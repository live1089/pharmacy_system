# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
		 # 包含数据库文件
        ('data/pharmacy.db', 'data'),
        ('data/backup.py', 'data'),
        ('data/clean_up_useless_data.py', 'data'),
        ('data/sqlite_data.py', 'data'),
        
        # 包含page_window下的所有模块
        ('page_window/*.py', 'page_window'),
		
		# 包含ui_app下的所有模块
		('ui_app/*.py', 'ui_app'),
	],
    hiddenimports=[
		 # 显式声明可能无法自动检测的依赖
        'sqlite3',
        'PySide6',
        'PySide6.QtWidgets',
        'PySide6.QtCore',
        'PySide6.QtGui',
        # 添加您的自定义模块
        'main_window',
        'login_window',
        'query_methods',
        'window_methods',
        'tools',
        'user_set_menu',
        'config_manager',
        # 添加page_window中的模块
        'page_window.inventory_count_page',
        'page_window.medicines_page',
        'page_window.purchase_page',
        'page_window.sell_medicines_page',
        'page_window.shelves_drug_page',
        'page_window.stock_medicines_page',
        'page_window.stock_out_page',
        'page_window.supplier_medicines_page',
        'page_window.system_formatting',
        'page_window.tools',
        'page_window.user_set_menu'
		
		# 添加ui_app中的模块
		 'ui_app.add_an_order_ui',
		 'ui_app.current_account_ui',
		 'ui_app.drug_add_ui',
		 'ui_app.drug_attribute_ui',
		 'ui_app.drug_entry_ui',
		 'ui_app.drug_purchase_add_ui',
		 'ui_app.drug_rormulation_ui',
		 'ui_app.drug_specification_ui',
		 'ui_app.drug_unit_ui',
		 'ui_app.inventory_count_entry_ui',
		 'ui_app.log_in_ui',
		 'ui_app.mainwondows_ui',
		 'ui_app.sell_drug_ui',
		 'ui_app.sell_list_ui',
		 'ui_app.shelves_drug_ui',
		 'ui_app.stock_all_ui',
		 'ui_app.stock_in_page_ui',
		 'ui_app.stock_locaton_ui',
		 'ui_app.stock_out_warehouse_drug_ui',
		 'ui_app.stock_out_warehouse_ui',
		 'ui_app.supplier_drug_ui',
		 'ui_app.sys_form_ui',
		 'ui_app.user_set_ui',
	],
	hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='PharmacyDrugManagement',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=['D:\\工具文档\\upx-5.0.1-win64\\upx'],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['Resize.ico'],
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PharmacyDrugManagement',
)