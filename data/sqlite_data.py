import sys
import os
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import Qt
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PySide6.QtWidgets import QMessageBox


class DatabaseInit(QSqlDatabase, QMessageBox):
    def __init__(self):
        super().__init__()
        documents_path = Path("E:/PharmacyDrugManagement")
        documents_path.mkdir(exist_ok=True)
        # 数据库文件路径
        db_path = str(documents_path / "pharmacy.db")

        # 初始化数据库连接
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(db_path)

        if not self.db.open():
            QMessageBox.critical(
                None, "数据库错误",
                f"无法打开数据库: {self.db.lastError().text()}"
            )
            sys.exit(1)

        query = QSqlQuery()

        query.exec("""
        CREATE TABLE IF NOT EXISTS medicine_dic(
                dic_id INTEGER PRIMARY KEY AUTOINCREMENT,     -- 新增主键
                trade_name TEXT NOT NULL,                     -- 商品名
                generic_name TEXT NOT NULL,                   -- 通用名
                specification_id INTEGER NOT NULL,            -- 规格型号ID
                manufacturer TEXT NOT NULL,                   -- 生产厂家
                formulation_id INTEGER NOT NULL,              -- 剂型
                approval_number TEXT,                 -- 批准文号(国药准字)
                category_id INTEGER NOT NULL,                 -- 分类ID
                unit_id INTEGER NOT NULL,                     -- 单位ID
                price REAL  CHECK (price >= 0),           -- 单价
                display_area_threshold INTEGER NOT NULL ,-- 陈列区阈值
                pharmacy_threshold INTEGER NOT NULL ,    -- 药库阈值
                FOREIGN KEY (category_id) REFERENCES MedicineCategories(category_id),
                FOREIGN KEY (specification_id) REFERENCES Specification(specification_id),
                FOREIGN KEY (formulation_id) REFERENCES drug_formulation(formulation_id),
                FOREIGN KEY (unit_id) REFERENCES drug_unit(unit_id),
                -- 确保基本药品信息唯一性
                UNIQUE (trade_name, approval_number)
        )
        """)

        query.exec("""
                CREATE TABLE IF NOT EXISTS drug_information_shelves (        -- 上架药品信息表
                drug_information_shelves_id INTEGER PRIMARY KEY AUTOINCREMENT,
                drug TEXT,                                                      -- 药品
                shelves_sum INTEGER,                                            -- 上架库存数量 (shelves_drug)
                warehouse_inventory_sum INTEGER,                                -- 仓库库存数量 (warehouse_shelf_position)
                shelves_location TEXT,                                          -- 上架位置
                warehouse_inventory_location TEXT,                              -- 库存位置
                approval_number TEXT                                -- 批准文号(国药准字)
        )
        """)

        # 更新药品信息货架上的上架插入
        query.exec("""
        CREATE TRIGGER IF NOT EXISTS update_drug_information_shelves_on_shelf_insert
            AFTER INSERT ON shelves_drug
            FOR EACH ROW
            BEGIN
                INSERT OR REPLACE INTO drug_information_shelves 
                (drug_information_shelves_id, drug, shelves_sum, warehouse_inventory_sum, 
                shelves_location, warehouse_inventory_location, approval_number)
                SELECT 
                    md.dic_id,
                    md.trade_name,
                    COALESCE((SELECT SUM(shelves_number) 
                             FROM shelves_drug 
                             WHERE drug = NEW.drug), 0),
                    COALESCE((SELECT SUM(quantity) 
                             FROM stock 
                             WHERE drug_id = NEW.drug), 0),
                    COALESCE(wsp.location, ''),
                    COALESCE((SELECT GROUP_CONCAT(wsp2.location, ', ') 
                    FROM warehouse_shelf_position wsp2 
                    JOIN stock s ON s.location = wsp2.warehouse_shelf_id 
                    WHERE s.drug_id = NEW.drug), ''),
                    md.approval_number
                FROM medicine_dic md
                JOIN stock_out_detail sod ON md.dic_id = sod.medicine_id
                JOIN stock_in_main sm ON sod.stock_batch = sm.in_id
                JOIN purchase_order po ON sm.order_id = po.order_id
                JOIN supplier su ON po.supplier_id = su.supplier_id
                LEFT JOIN warehouse_shelf_position wsp ON NEW.location_id = wsp.warehouse_shelf_id
                WHERE sod.detail_id = NEW.out_batch
                AND md.dic_id = NEW.drug
                LIMIT 1;
            END
        """)

        # 添加更新触发器
        query.exec("""
        CREATE TRIGGER IF NOT EXISTS update_drug_information_shelves_on_shelf_update
            AFTER UPDATE ON shelves_drug
            FOR EACH ROW
            BEGIN
                -- 更新新药品的信息
                INSERT OR REPLACE INTO drug_information_shelves 
                (drug_information_shelves_id, drug,shelves_sum, 
                 warehouse_inventory_sum, shelves_location, warehouse_inventory_location, approval_number)
                SELECT 
                    md.dic_id,
                    md.trade_name,
                    COALESCE((SELECT SUM(shelves_number) 
                             FROM shelves_drug 
                             WHERE drug = NEW.drug), 0),
                    COALESCE((SELECT SUM(quantity) 
                             FROM stock 
                             WHERE drug_id = NEW.drug), 0),
                    COALESCE((SELECT location FROM warehouse_shelf_position WHERE warehouse_shelf_id = NEW.location_id), ''),
                    COALESCE((SELECT GROUP_CONCAT(wsp2.location, ', ') 
                    FROM warehouse_shelf_position wsp2 
                    JOIN stock s ON s.location = wsp2.warehouse_shelf_id 
                    WHERE s.drug_id = NEW.drug), ''),
                    md.approval_number
                FROM medicine_dic md
                JOIN stock_out_detail sod ON md.dic_id = sod.medicine_id
                JOIN stock_in_main sm ON sod.stock_batch = sm.in_id
                JOIN purchase_order po ON sm.order_id = po.order_id
                JOIN supplier su ON po.supplier_id = su.supplier_id
                WHERE sod.detail_id = NEW.out_batch
                AND md.dic_id = NEW.drug
                LIMIT 1;
        
                -- 如果药品发生变化，也需要更新旧药品的信息
                INSERT OR REPLACE INTO drug_information_shelves 
                (drug_information_shelves_id, drug,shelves_sum, 
                 warehouse_inventory_sum, shelves_location, warehouse_inventory_location, approval_number)
                SELECT 
                    md.dic_id,
                    md.trade_name,
                    COALESCE((SELECT SUM(shelves_number) 
                             FROM shelves_drug 
                             WHERE drug = OLD.drug), 0),
                    COALESCE((SELECT SUM(quantity) 
                             FROM stock 
                             WHERE drug_id = OLD.drug), 0),
                    COALESCE((SELECT location FROM warehouse_shelf_position WHERE warehouse_shelf_id = OLD.location_id), ''),
                    COALESCE((SELECT GROUP_CONCAT(wsp2.location, ', ') 
                    FROM warehouse_shelf_position wsp2 
                    JOIN stock s ON s.location = wsp2.warehouse_shelf_id 
                    WHERE s.drug_id = OLD.drug), ''),
                    md.approval_number
                FROM medicine_dic md
                JOIN stock_out_detail sod ON md.dic_id = sod.medicine_id
                JOIN stock_in_main sm ON sod.stock_batch = sm.in_id
                JOIN purchase_order po ON sm.order_id = po.order_id
                JOIN supplier su ON po.supplier_id = su.supplier_id
                WHERE sod.detail_id = OLD.out_batch
                AND md.dic_id = OLD.drug
                LIMIT 1;
            END;
        """)

        query.exec("""
        -- 优化后的触发器，专门处理位置变化
        CREATE TRIGGER IF NOT EXISTS update_shelves_location_on_shelf_update
            AFTER UPDATE ON shelves_drug
            FOR EACH ROW
            WHEN OLD.location_id != NEW.location_id OR OLD.drug != NEW.drug
            BEGIN
                -- 更新新药品的位置信息
                UPDATE drug_information_shelves 
                SET shelves_location = COALESCE((SELECT location 
                                                FROM warehouse_shelf_position 
                                                WHERE warehouse_shelf_id = NEW.location_id), '')
                WHERE drug_information_shelves_id = NEW.drug;
        
                -- 如果药品ID也改变了，更新旧药品的位置信息
                UPDATE drug_information_shelves 
                SET shelves_location = COALESCE((SELECT location 
                                                FROM warehouse_shelf_position 
                                                WHERE warehouse_shelf_id = OLD.location_id), '')
                WHERE drug_information_shelves_id = OLD.drug AND OLD.drug != NEW.drug;
            END;
        """)

        # 添加上架药品删除触发器
        query.exec("""
        CREATE TRIGGER IF NOT EXISTS update_drug_information_shelves_on_shelf_delete
            AFTER DELETE ON shelves_drug
            FOR EACH ROW
            BEGIN
                INSERT OR REPLACE INTO drug_information_shelves 
                (drug_information_shelves_id, drug,shelves_sum, 
                 warehouse_inventory_sum, shelves_location, warehouse_inventory_location, approval_number)
                SELECT 
                    md.dic_id,
                    md.trade_name,
                    COALESCE((SELECT SUM(shelves_number) 
                             FROM shelves_drug 
                             WHERE drug = OLD.drug), 0),
                    COALESCE((SELECT SUM(quantity) 
                             FROM stock 
                             WHERE drug_id = OLD.drug), 0),
                    COALESCE(wsp.location, ''),
                    COALESCE((SELECT GROUP_CONCAT(wsp2.location, ', ') 
                    FROM warehouse_shelf_position wsp2 
                    JOIN stock s ON s.location = wsp2.warehouse_shelf_id 
                    WHERE s.drug_id = OLD.drug), ''),
                    md.approval_number
                FROM medicine_dic md
                JOIN stock_out_detail sod ON md.dic_id = sod.medicine_id
                JOIN stock_in_main sm ON sod.stock_batch = sm.in_id
                JOIN purchase_order po ON sm.order_id = po.order_id
                JOIN supplier su ON po.supplier_id = su.supplier_id
                LEFT JOIN warehouse_shelf_position wsp ON OLD.location_id = wsp.warehouse_shelf_id
                WHERE sod.detail_id = OLD.out_batch
                AND md.dic_id = OLD.drug
                LIMIT 1;
            END
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS drug_formulation(
                formulation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                formulation_name TEXT NOT NULL UNIQUE           -- 剂型名称（唯一约束）
        )""")

        query.exec("""
        CREATE TABLE IF NOT EXISTS drug_unit(
                unit_id INTEGER PRIMARY KEY AUTOINCREMENT,
                unit_name TEXT NOT NULL UNIQUE               -- 单位名称（唯一约束），粒/片/支等
        )""")

        query.exec("""
        CREATE TABLE IF NOT EXISTS Specification(
                specification_id INTEGER PRIMARY KEY AUTOINCREMENT,     -- 规格id
                packaging_specifications TEXT                --包装规格
        )""")

        query.exec(""" 
        CREATE TABLE IF NOT EXISTS MedicineCategories(          -- 药品分类表
                category_id INTEGER PRIMARY KEY AUTOINCREMENT,
                category_name TEXT NOT NULL UNIQUE
        )
        """)

        query.exec(""" 
        CREATE TABLE IF NOT EXISTS inventory_check(         
            check_id INTEGER PRIMARY KEY AUTOINCREMENT,
            medicine_id INTEGER NOT NULL,               -- 盘点药品
            inventory_of_batches INTEGER NOT NULL,      -- 盘点批次（库存批次）
            inventory_of_location INTEGER NOT NULL,     -- 盘点位置
            recorded_quantity INTEGER NOT NULL,         -- 盘点数量
            actual_quantity INTEGER NOT NULL,           -- 实际数量
            check_date DATE NOT NULL,                   -- 盘点日期
            discrepancy_reason TEXT,                    -- 差异原因（备注）
            FOREIGN KEY (medicine_id) REFERENCES medicine_dic (dic_id),
            FOREIGN KEY (inventory_of_batches) REFERENCES stock_in_main(in_id),
            FOREIGN KEY (inventory_of_location) REFERENCES warehouse_shelf_position(warehouse_shelf_id)
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS supplier (             -- 供应商信息表
            supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,      -- 供应商唯一标识ID
            name TEXT NOT NULL,                                 -- 供应商名字
            contact_person TEXT,                                -- 联系人
            phone TEXT,                                         -- 联系电话
            address TEXT,                                       -- 地址
            email TEXT,                                         -- 邮箱
            remarks TEXT,                                       -- 备注
            update_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,      -- 更新时间
            update_by TEXT,                                     -- 更新人
            create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,      -- 创建时间
            created_by TEXT                                     -- 创建人
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS purchase_order (                   -- 采购主表
                order_id INTEGER PRIMARY KEY AUTOINCREMENT,      -- 订单ID
                order_number TEXT NOT NULL,                      -- 订单号
                supplier_id INTEGER NOT NULL,                    -- 供应商ID
                order_date DATE NOT NULL DEFAULT CURRENT_DATE,   -- 下单日期
                expected_delivery_date DATE,                     -- 交货日期
                total_amount REAL,                               -- 订单总价
                remarks TEXT,                                    -- 备注
                FOREIGN KEY (supplier_id) REFERENCES supplier(supplier_id)
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS purchase_detail (                   -- 采购明细表（从表）
            detail_id INTEGER PRIMARY KEY AUTOINCREMENT,    -- 明细ID
            order_id INTEGER NOT NULL,                     -- 采购主表ID（外键）
            medicine_id INTEGER NOT NULL,                  -- 药品ID（外键）
            quantity INTEGER NOT NULL CHECK (quantity > 0),-- 采购数量
            purchase_total_price REAL NOT NULL CHECK ( purchase_total_price >= 0 ), --药品采购总价
            purchase_price REAL NOT NULL CHECK (purchase_price >= 0), -- 药品采购单价
            remarks TEXT,                                  -- 备注
            FOREIGN KEY (order_id) REFERENCES purchase_order(order_id),
            FOREIGN KEY (medicine_id) REFERENCES medicine_dic(dic_id)
        )
        """)

        # 入库主表
        query.exec("""
        CREATE TABLE IF NOT EXISTS stock_in_main (            -- 入库主表
                in_id INTEGER PRIMARY KEY AUTOINCREMENT,      -- 入库单ID
                order_id INTEGER,                             -- 关联采购订单ID
                in_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- 入库日期时间
                total_amount REAL,                            -- 入库总金额
                invoice_number TEXT,                          -- 发票号
                batch INTEGER NOT NULL,                       -- 批次
                production_lot_number INTEGER NOT NULL,       -- 生产批号
                validity DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,   -- 有效期
                remarks TEXT                                 -- 备注
        )
        """)

        # 入库明细表
        query.exec("""
        CREATE TABLE IF NOT EXISTS stock_in_detail (                                   -- 入库明细表
                detail_id INTEGER PRIMARY KEY AUTOINCREMENT,                           -- 明细ID
                in_id INTEGER NOT NULL,                                                -- 关联入库单ID 
                purchase_detail_id INTEGER NOT NULL,                                   -- 采购明细ID
                quantity INTEGER NOT NULL CHECK (quantity > 0),                        -- 入库数量
                actual_quantity INTEGER NOT NULL CHECK (actual_quantity > 0),          -- 实际入库数量
                warehouse_shelf_id INTEGER,                                            -- 存放位置
                FOREIGN KEY (in_id) REFERENCES stock_in_main(in_id),
                FOREIGN KEY (purchase_detail_id) REFERENCES purchase_detail(detail_id),
                FOREIGN KEY (warehouse_shelf_id) REFERENCES warehouse_shelf_position(warehouse_shelf_id),
                CHECK (actual_quantity <= quantity) -- 实际入库量≤采购量
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS warehouse_shelf_position(  --仓库货架位置
             warehouse_shelf_id INTEGER PRIMARY KEY AUTOINCREMENT,  -- ID
             location TEXT                        -- 位置
             )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS shelves_drug(
            shelves_id INTEGER PRIMARY KEY AUTOINCREMENT,
            outbound_number INTEGER,                        -- 出库单
            out_batch INTEGER,                              -- 出库批次
            drug INTEGER,                                   -- 药品
            shelves_number INTEGER,                         -- 上架数量
            location_id INTEGER,                            -- 上架位置
            FOREIGN KEY (out_batch) REFERENCES stock_out_detail(detail_id),
            FOREIGN KEY (drug) REFERENCES medicine_dic(dic_id),
            FOREIGN KEY (location_id) REFERENCES warehouse_shelf_position(warehouse_shelf_id)
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS stock_out_main (                -- 出库主表（记录出库单头信息）
                out_id INTEGER PRIMARY KEY AUTOINCREMENT,          -- 出库单ID
                outbound_number TEXT NOT NULL,                     -- 出库编号
                out_type TEXT NOT NULL CHECK (out_type IN ('调拨', '报损', '退货','上架')), -- 出库类型
                out_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- 出库日期时间
                total_amount REAL,                             -- 出库总数
                remarks TEXT                                  -- 备注
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS stock_out_detail (          -- 出库明细表（记录具体药品出库信息））
                detail_id INTEGER PRIMARY KEY AUTOINCREMENT,   -- 明细ID
                out_id INTEGER NOT NULL,                       -- 关联出库单ID
                medicine_id INTEGER NOT NULL,                  -- 药品ID
                stock_batch INTEGER NOT NULL,                  -- 入库批次（库存批次）
                out_batch TEXT not null,                       -- 出库批次
                quantity INTEGER NOT NULL,                     -- 出库数量
                time Date NOT NULL,                            -- 出库时间
                FOREIGN KEY (out_id) REFERENCES stock_out_main(out_id),
                FOREIGN KEY (medicine_id) REFERENCES medicine_dic(dic_id),
                FOREIGN KEY (stock_batch) REFERENCES stock_in_main(in_id)
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS inventory (                             -- 库存记录表
            inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,                -- 主键ID
            medicine_id INTEGER,                                           -- 对应的药品 ID（外键）
            detail_id INTEGER NOT NULL,                                    -- 入库明细表 （外键）
            quantity INTEGER,                                              -- 库存数量变化
            change_date DATE,                                              -- 库存变化日期
            change_type TEXT,                                              -- 变化类型
            batch_number TEXT,                                             -- 库存批次
            production_lot TEXT,                                           -- 生产批次
            FOREIGN KEY (medicine_id) REFERENCES medicine_dic(dic_id),
            FOREIGN KEY (detail_id) REFERENCES stock_in_detail(detail_id)
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS stock(                    -- 库存表
            stock_id INTEGER PRIMARY KEY AUTOINCREMENT,
            drug_id  INTEGER,                                -- 药品
            batch INTEGER NOT NULL,                          -- 药品批次
            location INT NOT NULL,                           -- 存储位置
            quantity INT NOT NULL CHECK (quantity >= 0),     -- 库存
            last_update DATETIME DEFAULT CURRENT_TIMESTAMP,  -- 更新时间
            FOREIGN KEY (batch) REFERENCES stock_in_main(in_id),
            FOREIGN KEY (location) REFERENCES warehouse_shelf_position(warehouse_shelf_id),
            FOREIGN KEY (drug_id) REFERENCES medicine_dic(dic_id)
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS users(                                   -- 用户信息表
            users_id INTEGER PRIMARY KEY AUTOINCREMENT,                     -- 主键ID
            username TEXT NOT NULL,                                         -- 用户名
            password TEXT NOT NULL,                                          -- 密码
            salt TEXT NOT NULL, 
            phone_number TEXT NOT NULL,                                     -- 手机号
            tip TEXT                                                        -- 提示词
        )
        """)

        query.exec("""
        CREATE TABLE IF NOT EXISTS expiring_medicines(
            expiring_medicine_id INTEGER PRIMARY KEY AUTOINCREMENT,
            batch_id INTEGER NOT NULL,                                -- 批次ID
            medicine_name TEXT NOT NULL,                              -- 药品名称
            expiry_date DATE NOT NULL,                                -- 药品的到期时间
            days_until_expiry INTEGER NOT NULL,                       -- 距离到期天数
            current_stock INTEGER NOT NULL,                           -- 当前仓库库存数量
            alert_threshold INTEGER DEFAULT 30,                       -- 预警阈值(天)
            status TEXT CHECK (status IN ('过期', '正常')),            -- 药品状态（过期 或 正常）
            last_updated DATETIME DEFAULT CURRENT_TIMESTAMP,          -- 最后更新时间
            FOREIGN KEY (batch_id) REFERENCES stock_in_main(in_id)
        )
        """)

        # 当药品入库时，更新有效期监控
        query.exec("""
        CREATE TRIGGER update_expiring_medicines_on_stock_in
            AFTER INSERT ON stock_in_detail
            FOR EACH ROW
            BEGIN
                -- 插入或更新临期药品监控数据
                INSERT OR REPLACE INTO expiring_medicines 
                (batch_id, medicine_name, expiry_date, days_until_expiry, current_stock, alert_threshold, status, last_updated)
                SELECT 
                    NEW.in_id,
                    md.trade_name,
                    sm.validity,
                    CAST(julianday(sm.validity) - julianday('now') AS INTEGER),
                    NEW.actual_quantity,
                    30,
                    CASE 
                        WHEN CAST(julianday(sm.validity) - julianday('now') AS INTEGER) < 0 THEN '过期'
                        ELSE '正常'
                    END,
                    datetime('now', '+8 hours')
                FROM medicine_dic md
                JOIN purchase_detail pd ON md.dic_id = pd.medicine_id
                JOIN stock_in_main sm ON sm.in_id = NEW.in_id
                WHERE pd.detail_id = NEW.purchase_detail_id
                ORDER BY sm.in_id DESC
                LIMIT 1;
            END;
        """)

        # 当药品入库修改变化时，更新临期药品监控数据
        query.exec("""
        CREATE TRIGGER update_expiring_medicines_on_stock_in_update
            AFTER UPDATE ON stock_in_main
            FOR EACH ROW
            WHEN OLD.validity != NEW.validity
            BEGIN
                -- 更新临期药品监控数据
                UPDATE expiring_medicines 
                SET expiry_date = NEW.validity,
                    days_until_expiry = CAST(julianday(NEW.validity) - julianday('now') AS INTEGER),
                    status = CASE 
                        WHEN CAST(julianday(NEW.validity) - julianday('now') AS INTEGER) < 0 THEN '过期'
                        ELSE '正常'
                    END,
                    last_updated = datetime('now', '+8 hours')
                WHERE batch_id = NEW.in_id;
            END;
        """)

        # 当药品入库仓库位置更新时更新药品上架信息表，库存表
        query.exec("""
        CREATE TRIGGER IF NOT EXISTS update_drug_information_shelves_on_stock_location_update
            AFTER UPDATE ON stock_in_detail
            FOR EACH ROW
            WHEN OLD.warehouse_shelf_id != NEW.warehouse_shelf_id
            BEGIN
                -- 更新 stock 表中的位置信息
                UPDATE stock
                SET location = NEW.warehouse_shelf_id,
                    last_update = datetime('now', '+8 hours')
                WHERE batch = NEW.in_id 
                AND drug_id = (
                    SELECT md.dic_id 
                    FROM purchase_detail pd 
                    JOIN medicine_dic md ON pd.medicine_id = md.dic_id 
                    WHERE pd.detail_id = NEW.purchase_detail_id
                );
                
                -- 更新 drug_information_shelves 表中的仓库库存位置信息
                UPDATE drug_information_shelves
                SET warehouse_inventory_location = (
                    SELECT GROUP_CONCAT(wsp.location, ', ')
                    FROM stock s
                    JOIN warehouse_shelf_position wsp ON s.location = wsp.warehouse_shelf_id
                    WHERE s.drug_id = (
                        SELECT md.dic_id 
                        FROM purchase_detail pd 
                        JOIN medicine_dic md ON pd.medicine_id = md.dic_id 
                        WHERE pd.detail_id = NEW.purchase_detail_id
                    )
                )
                WHERE drug_information_shelves_id = (
                    SELECT md.dic_id 
                    FROM purchase_detail pd 
                    JOIN medicine_dic md ON pd.medicine_id = md.dic_id 
                    WHERE pd.detail_id = NEW.purchase_detail_id
                );
            END;
        """)

        # --------------------------------------------------------------------------------------

        # 当药品入库主表删除时更新临期表
        query.exec("""
        CREATE TRIGGER cleanup_expiring_medicines_on_stock_in_delete
            AFTER DELETE ON stock_in_main
            FOR EACH ROW
            BEGIN
                -- 删除对应的临期药品监控记录
                DELETE FROM expiring_medicines 
                WHERE batch_id = OLD.in_id;

                -- 删除对应的库存记录
                DELETE FROM stock
                WHERE batch = OLD.in_id;

                -- 删除对应的入库明细记录
                DELETE FROM stock_in_detail
                WHERE in_id = OLD.in_id;
            END;
        """)

        # 当入库明细删除时更新相关表
        query.exec("""
        CREATE TRIGGER cleanup_related_data_on_stock_in_detail_delete
            AFTER DELETE ON stock_in_detail
            FOR EACH ROW
            BEGIN
                -- 删除对应的库存记录
                DELETE FROM stock
                WHERE batch = OLD.in_id AND location = OLD.warehouse_shelf_id;

                -- 删除对应的临期药品监控记录（如果该批次没有其他明细记录）
                DELETE FROM expiring_medicines 
                WHERE batch_id = OLD.in_id 
                AND NOT EXISTS (
                    SELECT 1 FROM stock_in_detail WHERE in_id = OLD.in_id
                );
            END;
        """)

        # --------------------------------------------------------------------------------------

        # 添加库存调整时更新临期药品的触发器
        query.exec("""
        CREATE TRIGGER update_expiring_medicines_on_stock_adjustment
            AFTER UPDATE ON stock
            FOR EACH ROW
            BEGIN
                -- 更新临期药品监控数据中的库存数量
                UPDATE expiring_medicines 
                SET current_stock = NEW.quantity,
                    status = CASE 
                        WHEN days_until_expiry < 0 THEN '过期'
                        ELSE '正常'
                    END,
                    last_updated = datetime('now', '+8 hours')
                WHERE batch_id = NEW.batch;
                
                -- 更新 drug_information_shelves 表中的仓库库存数量
                UPDATE drug_information_shelves
                SET warehouse_inventory_sum = (
                    SELECT COALESCE(SUM(s.quantity), 0)
                    FROM stock s
                    WHERE s.drug_id = NEW.drug_id
                )
                WHERE drug_information_shelves_id = NEW.drug_id;
            END;
        """)

        # 定期清理过期很久的药品监控记录
        query.exec("""
        CREATE TRIGGER cleanup_old_expired_medicines
            AFTER UPDATE ON expiring_medicines
            FOR EACH ROW
            WHEN NEW.days_until_expiry < -365
            BEGIN
                DELETE FROM expiring_medicines 
                WHERE expiring_medicine_id = NEW.expiring_medicine_id;
            END;
        """)

        # 入库后更新库存
        query.exec("""
            CREATE TRIGGER update_inventory_after_stock_in
                AFTER INSERT ON stock_in_detail
                FOR EACH ROW
                BEGIN
                    -- 确保记录库存变化历史
                    INSERT INTO inventory (medicine_id, detail_id, quantity, change_date, change_type, batch_number, production_lot)
                    SELECT 
                        COALESCE((SELECT md.dic_id 
                                 FROM purchase_detail pd 
                                 JOIN medicine_dic md ON md.dic_id = pd.medicine_id 
                                 WHERE pd.detail_id = NEW.purchase_detail_id), 0),
                        NEW.detail_id,
                        NEW.actual_quantity,
                        datetime('now','+8 hours'),
                        '入库',
                    (SELECT batch FROM stock_in_main WHERE in_id = NEW.in_id),
                    (SELECT production_lot_number FROM stock_in_main WHERE in_id = NEW.in_id)
                    WHERE EXISTS (
                        SELECT 1 
                        FROM purchase_detail pd 
                        JOIN medicine_dic md ON md.dic_id = pd.medicine_id 
                        WHERE pd.detail_id = NEW.purchase_detail_id
                    );
                    
                    -- 更新或插入 stock 表中的当前库存
                    INSERT OR REPLACE INTO stock (stock_id, drug_id, batch, location, quantity, last_update)
                    VALUES (
                        (SELECT stock_id 
                                 FROM stock 
                                 WHERE batch = NEW.in_id
                                 AND location = NEW.warehouse_shelf_id), 
 --                                (SELECT IFNULL(MAX(stock_id), 0) + 1 FROM stock)),
                        (SELECT md.dic_id 
                         FROM purchase_detail pd 
                         JOIN medicine_dic md ON md.dic_id = pd.medicine_id 
                         WHERE pd.detail_id = NEW.purchase_detail_id),
                        NEW.in_id,
                        NEW.warehouse_shelf_id,
                        COALESCE((SELECT quantity FROM stock WHERE batch = NEW.in_id AND location = NEW.warehouse_shelf_id), 0) + NEW.actual_quantity,
                        datetime('now', '+8 hours')
                    );
                END

        """)

        # 库存更新后更新库存
        query.exec("""
         CREATE TRIGGER update_inventory_after_stock_update
             AFTER UPDATE ON stock_in_detail
             FOR EACH ROW
             BEGIN
                 -- 更新库存变化历史
                 INSERT INTO inventory (medicine_id, detail_id, quantity, change_date, change_type)
                 SELECT 
                     (SELECT md.dic_id 
                      FROM purchase_detail pd 
                      JOIN medicine_dic md ON md.dic_id = pd.medicine_id 
                      WHERE pd.detail_id = NEW.purchase_detail_id),
                     NEW.detail_id,
                     NEW.actual_quantity - OLD.actual_quantity,  -- 只记录变化量
                     datetime('now','+8 hours'),
                     '库存调整'
                 WHERE EXISTS (
                     SELECT 1 
                     FROM purchase_detail pd 
                     JOIN medicine_dic md ON md.dic_id = pd.medicine_id 
                     WHERE pd.detail_id = NEW.purchase_detail_id
                 );

                 -- 更新 stock 表中的当前库存
                 UPDATE stock 
                 SET quantity = quantity + (NEW.actual_quantity - OLD.actual_quantity),
                       drug_id = (SELECT md.dic_id 
                        FROM purchase_detail pd 
                        JOIN medicine_dic md ON md.dic_id = pd.medicine_id 
                        WHERE pd.detail_id = NEW.purchase_detail_id),
                     last_update = datetime('now', '+8 hours')
                 WHERE batch = NEW.in_id AND location = NEW.warehouse_shelf_id;
             END
         """)

        # -------------------------------------------------------------------------------------------

        # 创建出库触发器
        query.exec("""
        -- 创建出库触发器
        CREATE TRIGGER stock_out_trigger
            AFTER INSERT ON stock_out_detail
            FOR EACH ROW
            BEGIN
                -- 记录库存变化历史（出库为负数）
                INSERT INTO inventory (medicine_id, detail_id, quantity, change_date, change_type, batch_number, production_lot)
                VALUES (
                    NEW.medicine_id,
                    NEW.detail_id,
                    -NEW.quantity,
                    datetime('now', '+8 hours'),
                    '出库',
                (SELECT batch FROM stock_in_main WHERE stock_in_main.in_id = NEW.stock_batch),
                (SELECT production_lot_number FROM stock_in_main WHERE stock_in_main.in_id = NEW.stock_batch)
                );
                
                -- 更新 stock 表中的库存数量
                UPDATE stock 
                SET quantity = quantity - NEW.quantity,
                    last_update = datetime('now', '+8 hours')
                WHERE batch = NEW.stock_batch 
                AND drug_id = NEW.medicine_id
                AND location IN (
                  SELECT warehouse_shelf_id 
                  FROM stock_in_detail 
                  WHERE stock_in_detail.in_id = NEW.stock_batch
                  ORDER BY detail_id DESC
                  LIMIT 1
                );
            END

        """)

        # 创建出库修改更新触发器
        query.exec("""
        CREATE TRIGGER IF NOT EXISTS update_inventory_after_stock_out_update
            AFTER UPDATE ON stock_out_detail
            FOR EACH ROW
            BEGIN
                -- 更新库存变化历史（记录修改前后的差值）
                INSERT INTO inventory (medicine_id, detail_id, quantity, change_date, change_type, batch_number, production_lot)
                VALUES (
                    NEW.medicine_id,
                    NEW.detail_id,
                    (OLD.quantity - NEW.quantity),  -- 记录数量变化（负值表示出库增加，正值表示出库减少）
                    datetime('now', '+8 hours'),
                    '出库修改',
                    (SELECT batch FROM stock_in_main WHERE in_id = NEW.stock_batch),
                    (SELECT production_lot_number FROM stock_in_main WHERE in_id = NEW.stock_batch)
                );

                -- 更新 stock 表中的库存数量（根据修改前后的差值调整）
                UPDATE stock 
                SET quantity = quantity + (OLD.quantity - NEW.quantity),
                    last_update = datetime('now', '+8 hours')
                WHERE batch = NEW.stock_batch 
                AND drug_id = NEW.medicine_id
                AND location IN (
                  SELECT warehouse_shelf_id 
                  FROM stock_in_detail 
                  WHERE in_id = NEW.stock_batch
                  ORDER BY detail_id DESC
                  LIMIT 1
                );
            END
        """)

        # 删除出库记录的触发器
        query.exec("""
        CREATE TRIGGER IF NOT EXISTS update_inventory_after_stock_out_delete
            AFTER DELETE ON stock_out_detail
            FOR EACH ROW
            BEGIN
                -- 记录库存变化历史（删除出库记录，相当于减少出库量）
                INSERT INTO inventory (medicine_id, detail_id, quantity, change_date, change_type, batch_number, production_lot)
                VALUES (
                    OLD.medicine_id,
                    OLD.detail_id,
                    OLD.quantity,  -- 正数表示库存增加（因为删除了出库记录）
                    datetime('now', '+8 hours'),
                    '出库删除',
                    (SELECT batch FROM stock_in_main WHERE in_id = OLD.stock_batch),
                    (SELECT production_lot_number FROM stock_in_main WHERE in_id = OLD.stock_batch)
                );

                -- 更新 stock 表中的库存数量（增加库存，因为删除了出库记录）
                UPDATE stock 
                SET quantity = quantity + OLD.quantity,
                    last_update = datetime('now', '+8 hours')
                WHERE batch = OLD.stock_batch 
                AND drug_id = OLD.medicine_id
                AND location IN (
                  SELECT warehouse_shelf_id 
                  FROM stock_in_detail 
                  WHERE in_id = OLD.stock_batch
                  ORDER BY detail_id DESC
                  LIMIT 1
                );
            END
        """)

        # ----------------------------------------------------------------------------------------------------

        # 库存盘点插入触发器 - 用于更新上架库存
        query.exec("""
         CREATE TRIGGER IF NOT EXISTS insert_shelves_inventory_on_check
            AFTER INSERT ON inventory_check
            FOR EACH ROW
            WHEN EXISTS (SELECT 1 FROM shelves_drug WHERE location_id = NEW.inventory_of_location)
            BEGIN
                -- 更新上架库存
                UPDATE shelves_drug 
                SET shelves_number = NEW.recorded_quantity
                WHERE drug = NEW.medicine_id 
                AND location_id = NEW.inventory_of_location;
            END;
        """)

        # 库存盘点插入触发器 - 用于更新仓库库存
        query.exec("""
        CREATE TRIGGER IF NOT EXISTS insert_warehouse_inventory_on_check
            AFTER INSERT ON inventory_check
            FOR EACH ROW
            WHEN NOT EXISTS (SELECT 1 FROM shelves_drug WHERE location_id = NEW.inventory_of_location)
            BEGIN
                -- 更新仓库库存
                UPDATE stock 
                SET quantity = NEW.recorded_quantity
                WHERE drug_id = NEW.medicine_id 
                AND location = NEW.inventory_of_location 
                AND batch = NEW.inventory_of_batches;
            END;
        """)

        # 库存盘点更新触发器 - 用于更新上架库存
        query.exec("""
        CREATE TRIGGER IF NOT EXISTS update_shelves_inventory_on_check
        AFTER UPDATE ON inventory_check
        FOR EACH ROW
        WHEN EXISTS (SELECT 1 FROM shelves_drug WHERE location_id = NEW.inventory_of_location)
        BEGIN
            -- 更新上架库存
            UPDATE shelves_drug 
            SET shelves_number = NEW.recorded_quantity
            WHERE drug = NEW.medicine_id 
            AND location_id = NEW.inventory_of_location;
        END;
        """)

        # 库存盘点更新触发器 - 用于更新仓库库存
        query.exec("""
        CREATE TRIGGER IF NOT EXISTS update_warehouse_inventory_on_check
            AFTER UPDATE ON inventory_check
            FOR EACH ROW
            WHEN NOT EXISTS (SELECT 1 FROM shelves_drug WHERE location_id = NEW.inventory_of_location)
            BEGIN
                -- 更新仓库库存
                UPDATE stock 
                SET quantity = NEW.recorded_quantity
                WHERE drug_id = NEW.medicine_id 
                AND location = NEW.inventory_of_location 
                AND batch = NEW.inventory_of_batches;
            END;
        """)


# 基表模型
class BaseTableModel(QSqlTableModel):
    def __init__(self, parent=None, db=None, table_name="", headers=None, hidden_columns=None):
        super().__init__(parent, db)
        # 设置表名
        self.setTable(table_name)

        self.setQuery(f"SELECT * FROM {table_name} LIMIT 100")

        # 检查表是否存在并可以访问
        if not self.select():
            print(f"无法从表 {table_name} 加载数据: {self.lastError().text()}")
        else:
            print(f"成功加载表 {table_name}，行数: {self.rowCount()}")

        # 设置表头
        if headers:
            for col_index, header_text in headers.items():
                self.setHeaderData(col_index, Qt.Orientation.Horizontal, header_text)

        # 记录隐藏列
        self.hidden_columns = hidden_columns or []

    def get_primary_key_column(self):
        """获取表的主键列名（只取第一个主键）"""
        # 尝试从隐藏列中查找主键
        for col in self.hidden_columns:
            if "id" in self.headerData(col, Qt.Orientation.Horizontal).lower():
                return self.record().fieldName(col)

        # 没有找到，则查询数据库元数据
        query = QSqlQuery(self.database())
        query.exec(f"PRAGMA table_info({self.tableName()})")

        while query.next():
            # name(1), type(2), pk(5)
            if query.value(5) > 0:  # pk列不为0
                return query.value(1)

        # 默认返回 "id"（常见主键名称）
        return "id"


# 上架药品信息
class ShelvesDrugsMessageModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "药品名称",
        2: "上架库存数量",
        3: "仓库库存数量",
        4: "上架位置",
        5: "库存位置",
        6: "批准文号",
    }
    HIDDEN_COLUMNS = [0]

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="drug_information_shelves",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS,
        )


class StockAllModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "药品",
        2: "库存批次",
        3: "存储位置",
        4: "库存",
        5: "更新时间"
    }
    HIDDEN_COLUMNS = [0]  # 隐藏的列索引

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="stock",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS,
        )


# 临期模型
class ExpiringMedicineModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "库存批次",
        2: "药品名称",
        3: "药品到期时间",
        4: "距离到期天数",
        5: "当前仓库库存数量",
        6: "预警阈值(天)",
        7: "药品状态",
        8: "最后更新时间"
    }
    HIDDEN_COLUMNS = [0]

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="expiring_medicines",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


# 供应商模式
class SupplierModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "名称",
        2: "联系人",
        3: "电话",
        4: "地址",
        5: "邮箱",
        6: "备注",
        7: "更新时间",
        8: "更新人",
        9: "创建时间",
        10: "创建人"
    }
    HIDDEN_COLUMNS = [0]  # 隐藏的列索引

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="supplier",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


# 采购订单模式
class PurchaseOrderModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "订单号",
        2: "供应商",
        3: "下单日期",
        4: "交货日期",
        5: "采购总价",
        6: "备注"
    }
    HIDDEN_COLUMNS = [0]  # 隐藏的列索引

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="purchase_order",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )

    def get_primary_key_column(self):
        for col in self.HEADERS.keys():
            if "id" in self.headerData(col, Qt.Orientation.Horizontal).lower():
                return self.record().fieldName(col)
        return "id"


# 采购明细模式
class PurchaseDetailModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "订单编号",
        2: "药品",
        3: "采购数量",
        4: "药品采购总价",
        5: "药品采购单价",
        6: "售价",
        7: "下单时间",
        8: "备注"
    }
    HIDDEN_COLUMNS = [0]  # 隐藏的列索引

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="purchase_detail",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


# 库存记录模型
class InventoryModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "药品名称",
        2: "库存数量变化",
        3: "库存变化日期",
        4: "变化类型",
        5: "库存批次",
        6: "生产批次"
    }
    HIDDEN_COLUMNS = [0]

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="inventory",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


# 入库主模型
class StockInMainModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "采购订单",
        2: "供应商",
        3: "入库日期",
        4: "入库总金额",
        5: "发票号",
        6: "批次",
        7: "生产批号",
        8: "有效期",
        9: "备注"
    }
    HIDDEN_COLUMNS = [0]

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="stock_in_main",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


# 入库明细模式
class StockInDetailModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "订单号",
        2: "药品",
        3: "有效期",
        4: "采购单价",
        5: "销售单价",
        6: "入库数量",
        7: "实际入库数量",
        8: "货位/库存位置",
        9: "当前库存",
        10: "批次",
        11: "生产批号"
    }
    HIDDEN_COLUMNS = [0]

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="stock_in_detail",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


# 库存批次模式
class InventoryDatchModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "批次",
        2: "生产批号",
        3: "入库明细表",
        4: "药品",
        5: "有效期",
        6: "当前库存",
        7: "货位/存放位置",
        8: "创建时间",
        9: "最后更新时间"
    }
    HIDDEN_COLUMNS = [0]

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="inventory_batch",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


# 出库主模型
class StockOutMainModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "出库编号",
        2: "出库类型",
        3: "出库日期",
        4: "出库总数",
        5: "备注",
    }
    HIDDEN_COLUMNS = [0]

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="stock_out_main",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


# 出库明细模式
class StockOutDetailModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "出库编号",
        2: "药品",
        3: "库存批次",
        4: "出库批次",
        5: "出库数量",
        6: "出库时间"
    }
    HIDDEN_COLUMNS = [0]

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="stock_out_detail",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )

    def get_primary_key_column(self):
        # 明确指定主键列名
        return "detail_id"


# 库存盘点模式
class InventoryCheckModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "药品名称",
        2: "盘点的库存批次",
        3: "盘点位置",
        4: "盘点数量",
        5: "库存数量",
        6: "盘点日期",
        7: "备注说明"
    }
    HIDDEN_COLUMNS = [0]

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="inventory_check",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


class MedicineCategoriesModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "类型"
    }
    HIDDEN_COLUMNS = [0]

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="MedicineCategories",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


class StockLocationModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "位置"
    }
    HIDDEN_COLUMNS = [0]

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="warehouse_shelf_position",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


class DrugRormulationModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "剂型"
    }
    HIDDEN_COLUMNS = [0]

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="drug_formulation",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


class DrugUnitModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "单位"
    }
    HIDDEN_COLUMNS = [0]

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="drug_unit",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


class SpecificationModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "剂型",
        2: "药品单位",
        3: "包装规格",
    }
    HIDDEN_COLUMNS = [0, 1, 2]

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="Specification",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


class DrugDicModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "药品",
        2: "通用名",
        3: "规格型号",
        4: "生产厂家",
        5: "剂型",
        6: "国药准字",
        7: "分类",
        8: "单位",
        9: "价格",
        10: "上架预警阈值",
        11: "库存预警阈值",
    }
    HIDDEN_COLUMNS = [0]

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="medicine_dic",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


# 上架药品
class ShelvesDrugModel(BaseTableModel):
    HEADERS = {
        0: "ID",
        1: "出库单",
        2: "出库批次",
        3: "药品",
        4: "数量",
        5: "货位",
        6: "库存批次",
        7: "有效期"
    }
    HIDDEN_COLUMNS = [0]

    def __init__(self, parent=None, db=None):
        super().__init__(
            parent=parent,
            db=db,
            table_name="shelves_drug",
            headers=self.HEADERS,
            hidden_columns=self.HIDDEN_COLUMNS
        )


def shelves_stock_model(self):
    """获取上架药品库存模型"""
    sql = """
         SELECT
            e.shelves_id,
            md.trade_name,
            SUM(e.shelves_number),
            wsp.location,
            sma.batch as 库存批次,
            sma.validity as 有效期
        FROM shelves_drug e
        LEFT JOIN stock_out_detail sd ON e.out_batch = sd.detail_id
        LEFT JOIN medicine_dic md ON e.drug = md.dic_id
        LEFT JOIN stock_in_main sma ON sd.stock_batch = sma.in_id
        LEFT JOIN warehouse_shelf_position wsp ON e.location_id = wsp.warehouse_shelf_id
        GROUP BY md.trade_name, sma.batch, wsp.location
    """
    # 创建模型并设置查询
    model = QSqlQueryModel(self)
    model.setQuery(sql, self.db)
    return model


# 上架模型
def get_shelves_drug_model(self):
    self.shelves_model = ShelvesDrugModel(self, self.db)
    sql = """
        SELECT
            e.shelves_id,
            sm.outbound_number,
            sd.out_batch,
            md.trade_name,
            e.shelves_number,
            wsp.location,
            sma.batch as 库存批次,
            sma.validity as 有效期
        FROM shelves_drug e
        LEFT JOIN stock_out_detail sd ON e.out_batch = sd.detail_id
        LEFT JOIN stock_in_main sma ON sd.stock_batch = sma.in_id
        LEFT JOIN medicine_dic md ON e.drug = md.dic_id
        LEFT JOIN warehouse_shelf_position wsp ON e.location_id = wsp.warehouse_shelf_id
        LEFT JOIN stock_out_main sm ON e.outbound_number = sm.out_id
    """
    self.shelves_model.setQuery(sql, self.db)
    self.drugs_on_shelves_tableView.setModel(self.shelves_model)
    for col in self.shelves_model.HIDDEN_COLUMNS:
        self.drugs_on_shelves_tableView.hideColumn(col)

    return self.shelves_model


def get_medicine_dic_model(self):
    self.medicine_dic_model = DrugDicModel(self, self.db)
    sql = f"""
        SELECT
            e.dic_id,
            e.trade_name,
            e.generic_name,
            d.packaging_specifications  as 规格,
            e.manufacturer,
            f.formulation_name as 剂型,
            e.approval_number,
            m.category_name as 分类,
            u.unit_name as 单位,
            e.price,
            e.display_area_threshold,
            e.pharmacy_threshold
        FROM medicine_dic e
        LEFT JOIN Specification d ON e.specification_id = d.specification_id
        LEFT JOIN drug_unit u ON e.unit_id = u.unit_id
        LEFT JOIN drug_formulation f ON e.formulation_id = f.formulation_id
        LEFT JOIN MedicineCategories m ON e.category_id = m.category_id
    """
    self.medicine_dic_model.setQuery(sql, self.db)
    self.drug_dic_tableView.setModel(self.medicine_dic_model)
    for col in self.medicine_dic_model.HIDDEN_COLUMNS:
        self.drug_dic_tableView.hideColumn(col)

    return self.medicine_dic_model


# 临期
def get_expiring_medicine_model(self):
    self.expiring_medicine_model = ExpiringMedicineModel(self, self.db)
    # 使用参数化查询，并考虑用户设置的阈值
    sql = """
        SELECT
            e.expiring_medicine_id,
            st.batch,
            e.medicine_name,
            e.expiry_date,
            e.days_until_expiry,
            e.current_stock,
            e.alert_threshold,
            e.status,
            e.last_updated
        FROM expiring_medicines e
        LEFT JOIN stock_in_main st ON e.batch_id = st.in_id
        WHERE e.days_until_expiry <= COALESCE(e.alert_threshold, 60)
        ORDER BY e.days_until_expiry
    """
    self.expiring_medicine_model.setQuery(sql, self.db)
    self.expiring_drugs_tableView.setModel(self.expiring_medicine_model)

    # 应用隐藏列
    for col in self.expiring_medicine_model.hidden_columns:
        self.expiring_drugs_tableView.hideColumn(col)

    return self.expiring_medicine_model


# 入库主模型
def get_stock_in_main_model(self, storage_start_date, storage_end_date):
    self.stock_in_main_model = StockInMainModel(self, self.db)
    sql = f"""
        SELECT
            s.in_id,
            p.order_number,
            r.name,
            s.in_date,
            s.total_amount,
            s.invoice_number,
            s.batch,
            s.production_lot_number,
            s.validity,
            s.remarks as 备注
        FROM stock_in_main s
        LEFT JOIN  purchase_order p ON s.order_id = p.order_id
        Left join  supplier r ON p.supplier_id = r.supplier_id
        WHERE s.in_date BETWEEN '{storage_start_date}' AND '{storage_end_date}'
    """
    self.stock_in_main_model.setQuery(sql, self.db)
    self.main_tableView.setModel(self.stock_in_main_model)
    for col in self.stock_in_main_model.hidden_columns:
        self.main_tableView.hideColumn(col)

    return self.stock_in_main_model


# 入库明细模型
def get_stock_in_detail_model(self, storage_start_date, storage_end_date):
    self.stock_in_detail_model = StockInDetailModel(self, self.db)
    sql = f"""
        SELECT
            s.detail_id,
            o.order_number,
            dic.trade_name,
            m.validity,
            pu.purchase_price,
            dic.price,
            s.quantity as 入库数量,
            s.actual_quantity as 实际入库数量,
            i.location as 库存位置,
            st.quantity as 库存数量,
            m.batch as 库存批次,
            m.production_lot_number as 生产批号,
            m.in_date as 入库时间
        FROM stock_in_detail s
        LEFT JOIN stock_in_main m ON s.in_id = m.in_id
        LEFT JOIN purchase_detail pu ON s.purchase_detail_id = pu.detail_id
        LEFT JOIN purchase_order o ON m.order_id = o.order_id
        LEFT JOIN medicine_dic dic ON pu.medicine_id = dic.dic_id
        LEFT JOIN warehouse_shelf_position i ON s.warehouse_shelf_id = i.warehouse_shelf_id
        LEFT JOIN stock st ON st.batch = s.in_id AND st.location = s.warehouse_shelf_id
        WHERE m.in_date BETWEEN '{storage_start_date}' AND '{storage_end_date}'
    """
    self.stock_in_detail_model.setQuery(sql, self.db)
    self.detail_tableView.setModel(self.stock_in_detail_model)
    for col in self.stock_in_detail_model.hidden_columns:
        self.detail_tableView.hideColumn(col)

    return self.stock_in_detail_model


# 出库主模型
def get_stock_out_main_model(self, start_date, end_date):
    self.stock_out_main_model = StockOutMainModel(self, self.db)
    sql = f"""
        SELECT
            s.out_id,
            s.outbound_number,
            s.out_type,
            s.out_date,
            s.total_amount,
            s.remarks
        FROM stock_out_main s
        WHERE s.out_date BETWEEN '{start_date}' AND '{end_date}'
        """
    self.stock_out_main_model.setQuery(sql, self.db)
    self.stock_out_main_tableView.setModel(self.stock_out_main_model)
    for col in self.stock_out_main_model.hidden_columns:
        self.stock_out_main_tableView.hideColumn(col)
    return self.stock_out_main_model


# 出库明细模型
def get_stock_out_detail_model(self, start_date, end_date):
    self.stock_out_detail_model = StockOutDetailModel(self, self.db)
    sql = f"""
        SELECT
            s.detail_id,
            sm.outbound_number,
            dic.trade_name,
            st.batch,
            s.out_batch,
            s.quantity,
            s.time,
            st.in_date as 入库时间
        FROM stock_out_detail s
        LEFT JOIN stock_out_main sm ON s.out_id = sm.out_id
        LEFT JOIN medicine_dic dic ON s.medicine_id = dic.dic_id
        LEFT JOIN stock_in_main st ON s.stock_batch = st.in_id
        WHERE sm.outbound_number IS NOT NULL 
        AND sm.outbound_number != ''
        AND sm.out_date BETWEEN '{start_date}' AND '{end_date}'
    """
    self.stock_out_detail_model.setQuery(sql, self.db)
    self.stock_out_detail_tableView.setModel(self.stock_out_detail_model)
    for col in self.stock_out_detail_model.hidden_columns:
        self.stock_out_detail_tableView.hideColumn(col)
    return self.stock_out_detail_model


# 供应商
def get_supplier_model(self):
    self.supplier_model = SupplierModel(self, self.db)
    self.supplier_tableView.setModel(self.supplier_model)

    # 应用隐藏列
    for col in self.supplier_model.hidden_columns:
        self.supplier_tableView.hideColumn(col)

    return self.supplier_model


# 采购订单
def get_purchase_order_model(self, pur_start_date, pur_end_date):
    self.purchase_order_model = PurchaseOrderModel(self, self.db)
    sql = f"""
        SELECT
            pur.order_id,
            pur.order_number,
            de.name,
            pur.order_date,
            pur.expected_delivery_date,
            pur.total_amount,
            pur.remarks
        FROM purchase_order pur
        LEFT JOIN supplier de ON pur.supplier_id = de.supplier_id
        LEFT JOIN purchase_order ord ON pur.order_id = ord.order_id
        WHERE pur.order_date BETWEEN '{pur_start_date}' AND '{pur_end_date}'
    """
    self.purchase_order_model.setQuery(sql, self.db)
    self.purchase_order_tableView.setModel(self.purchase_order_model)
    for col in self.purchase_order_model.hidden_columns:
        self.purchase_order_tableView.hideColumn(col)

    return self.purchase_order_model


# 采购订单明细
def get_purchase_order_detail_model(self, pur_start_date, pur_end_date):
    self.purchase_order_detail_model = PurchaseDetailModel(self, self.db)
    sql = f"""
        SELECT
            pur.detail_id,
            ord.order_number,
            de.trade_name,
            pur.quantity,
            pur.purchase_total_price,
            pur.purchase_price,
            de.price as 售价,
            ord.order_date as 下单时间,
            pur.remarks as 备注  
        FROM purchase_detail pur
        LEFT JOIN medicine_dic de ON pur.medicine_id = de.dic_id
        LEFT JOIN purchase_order ord ON pur.order_id = ord.order_id
        WHERE ord.order_date BETWEEN '{pur_start_date}' AND '{pur_end_date}'
    """
    self.purchase_order_detail_model.setQuery(sql, self.db)
    self.purchase_detail_tableView.setModel(self.purchase_order_detail_model)
    for col in self.purchase_order_detail_model.hidden_columns:
        self.purchase_detail_tableView.hideColumn(col)
    return self.purchase_order_detail_model


# 库存记录
def get_inventory_model(self, start_date, end_date):
    self.inventory_model = InventoryModel(self, self.db)
    sql = f"""
        SELECT
            inv.inventory_id,
            de.trade_name,
            inv.quantity,
            inv.change_date,
            inv.change_type,
            inv.batch_number,
            inv.production_lot as 生产批号
        FROM inventory inv
        LEFT JOIN medicine_dic de ON inv.medicine_id = de.dic_id
        WHERE inv.change_date BETWEEN '{start_date}' AND '{end_date}'
    """
    self.inventory_model.setQuery(sql, self.db)
    self.inventory_tableView.setModel(self.inventory_model)
    for col in self.inventory_model.hidden_columns:
        self.inventory_tableView.hideColumn(col)

    return self.inventory_model


# 库存盘点
def get_inventory_check(self, start_date, end_date):
    self.inventory_check_model = InventoryCheckModel(self, self.db)
    sql = f"""
        SELECT
            inv.check_id,
            de.trade_name,
            sta.batch,
            ws.location as 库存位置,
            inv.recorded_quantity,
            inv.actual_quantity,
            inv.check_date,
            inv.discrepancy_reason
        FROM inventory_check inv
        LEFT JOIN medicine_dic de ON inv.medicine_id = de.dic_id
        LEFT JOIN stock_in_main sta ON inv.inventory_of_batches = sta.in_id
        LEFT JOIN warehouse_shelf_position ws ON ws.warehouse_shelf_id = inv.inventory_of_location
        WHERE inv.check_date BETWEEN '{start_date}' AND '{end_date}'
    """
    self.inventory_check_model.setQuery(sql, self.db)
    self.inventory_check_tableView.setModel(self.inventory_check_model)
    for col in self.inventory_check_model.hidden_columns:
        self.inventory_check_tableView.hideColumn(col)

    return self.inventory_check_model


# 上架药品信息
def get_shelves_drug_message_model(self):
    self.shelves_drug_model = ShelvesDrugsMessageModel(self, self.db)
    sql = """
        SELECT
            d.drug_information_shelves_id,
            d.drug,
            d.shelves_sum,
            d.warehouse_inventory_sum,
            d.shelves_location,
            d.warehouse_inventory_location,
            d.approval_number
        FROM drug_information_shelves d
        ORDER BY d.drug
        """
    self.shelves_drug_model.setQuery(sql, self.db)
    self.shelves_drug_tableView.setModel(self.shelves_drug_model)
    for col in self.shelves_drug_model.hidden_columns:
        self.shelves_drug_tableView.hideColumn(col)
    return self.shelves_drug_model


# ========================================================================================


def get_shelves_stock_model(self):
    """获取上架药品库存模型并设置到表格视图"""
    model = shelves_stock_model(self)  # 使用主窗口的数据库连接
    self.shelves_stock_tableView.setModel(model)

    # 设置表头
    model.setHeaderData(0, Qt.Orientation.Horizontal, "ID")
    model.setHeaderData(1, Qt.Orientation.Horizontal, "药品名称")
    model.setHeaderData(2, Qt.Orientation.Horizontal, "上架数量")
    model.setHeaderData(3, Qt.Orientation.Horizontal, "上架位置")
    model.setHeaderData(4, Qt.Orientation.Horizontal, "库存批次")
    model.setHeaderData(5, Qt.Orientation.Horizontal, "有效期")

    # 隐藏ID列
    self.shelves_stock_tableView.hideColumn(0)
    return model


def get_stock_in_all_model(self):
    self.stock_all = StockAllModel(self, self.db)
    sql = f"""
        SELECT
            s.stock_id,
            dic.trade_name,
            us.batch,
            ud.location,
            s.quantity,
            s.last_update,
            us.validity as 有效期,
            us.production_lot_number as 生产批号
        FROM stock s
        LEFT JOIN stock_in_main us ON us.in_id = s.batch
        LEFT JOIN warehouse_shelf_position ud ON ud.warehouse_shelf_id = s.location
        LEFT JOIN medicine_dic dic ON dic.dic_id = s.drug_id
    """
    self.stock_all.setQuery(sql, self.db)
    self.stock_all_tableView.setModel(self.stock_all)
    for col in self.stock_all.hidden_columns:
        self.stock_all_tableView.hideColumn(col)
    return self.stock_all


def setup_warning_display(self):
    """设置陈列区低库存预警显示（基于每个药品的个性化阈值）"""
    try:
        # 直接查询陈列区低库存预警数据
        sql = """
            SELECT 
                md.dic_id as 药品ID,
                md.trade_name as 药品名称,
                sim.batch as 库存批次,
                s.shelves_number as 上架库存,
                GROUP_CONCAT(DISTINCT wsp.location) as 存放位置,
                md.display_area_threshold as 预警阈值
            FROM medicine_dic md
            LEFT JOIN shelves_drug s ON s.drug = md.dic_id
            LEFT JOIN stock_out_detail sod on s.out_batch = sod.detail_id
            LEFT JOIN stock_in_main sim on sod.stock_batch = sim.in_id
            LEFT JOIN warehouse_shelf_position wsp on s.location_id = wsp.warehouse_shelf_id
            WHERE s.shelves_number< md.display_area_threshold
            GROUP BY md.dic_id, md.trade_name, sim.batch
            ORDER BY md.trade_name, sim.batch
        """

        model = QSqlQueryModel(self)
        model.setQuery(sql, self.db)

        self.warning_display_area_tableView.setModel(model)

        # 添加调试信息
        print(f"陈列区预警数据行数: {model.rowCount()}")

        # 隐藏ID列（第一列）
        self.warning_display_area_tableView.hideColumn(0)
        return model
    except Exception as e:
        print(f"设置陈列区预警显示时出错: {e}")
        return None


def setup_warning_stock(self):
    """设置药库低库存预警显示（基于每个药品的个性化阈值）"""
    try:
        # 直接查询药库低库存预警数据
        sql = """
            SELECT 
                md.dic_id as 药品ID,
                md.trade_name as 药品名称,
                sim.batch as 库存批次,
                s.quantity as 仓库库存,
                GROUP_CONCAT(DISTINCT wsp.location) as 存放位置,
                md.pharmacy_threshold as 预警阈值
            FROM medicine_dic md
            LEFT JOIN main.stock s on s.drug_id = md.dic_id
            LEFT JOIN stock_in_main sim on s.batch = sim.in_id
            LEFT JOIN warehouse_shelf_position wsp on s.location = wsp.warehouse_shelf_id
            WHERE s.quantity < md.pharmacy_threshold
            GROUP BY md.dic_id, md.trade_name, sim.batch
            ORDER BY md.trade_name, sim.batch
        """

        model = QSqlQueryModel(self)
        model.setQuery(sql, self.db)

        self.stock_warning_drug_tableView.setModel(model)

        # 添加调试信息
        print(f"药库预警数据行数: {model.rowCount()}")

        # 隐藏ID列（第一列）
        self.stock_warning_drug_tableView.hideColumn(0)
        return model
    except Exception as e:
        print(f"设置药库预警显示时出错: {e}")
        return None


