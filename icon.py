import base64

with open("Res.ico", "rb") as f:
    icon_data = base64.b64encode(f.read()).decode("utf-8")

with open("icon_data.py", "w") as f:
    f.write(f"icon_data = {repr(icon_data)}")