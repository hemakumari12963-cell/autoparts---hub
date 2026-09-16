from flask import Flask
app = Flask(__name__)

# 32 PRODUCTS - 4 CATEGORY
products = [
    # --- ENGINE PARTS (8) ---
    {"cat":"Engine","name":"Bosch Spark Plug","price":"₹199","mrp":"₹350","img":"https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?w=400","rating":"4.5"},
    {"cat":"Engine","name":"Castrol Engine Oil 3.5L","price":"₹1,499","mrp":"₹2,100","img":"https://images.unsplash.com/photo-1603386329225-868f9b1ee6c9?w=400","rating":"4.8"},
    {"cat":"Engine","name":"Air Filter - Swift","price":"₹299","mrp":"₹550","img":"https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=400","rating":"4.3"},
    {"cat":"Engine","name":"Oil Filter","price":"₹249","mrp":"₹400","img":"https://images.unsplash.com/photo-1600880292089-90a7e086ee0c?w=400","rating":"4.4"},
    {"cat":"Engine","name":"Radiator Coolant","price":"₹399","mrp":"₹600","img":"https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?w=400","rating":"4.6"},
    {"cat":"Engine","name":"Timing Belt","price":"₹1,199","mrp":"₹1,800","img":"https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=400","rating":"4.2"},
    {"cat":"Engine","name":"Fuel Pump","price":"₹2,499","mrp":"₹3,500","img":"https://images.unsplash.com/photo-1603386329225-868f9b1ee6c9?w=400","rating":"4.7"},
    {"cat":"Engine","name":"Alternator","price":"₹4,999","mrp":"₹7,000","img":"https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?w=400","rating":"4.5"},

    # --- BODY PARTS (8) ---
    {"cat":"Body","name":"Front Bumper - White","price":"₹3,499","mrp":"₹5,000","img":"https://images.unsplash.com/photo-1551524559-8af4e6624178?w=400","rating":"4.4"},
    {"cat":"Body","name":"Side Mirror Pair","price":"₹899","mrp":"₹1,400","img":"https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=400","rating":"4.3"},
    {"cat":"Body","name":"Door Handle Chrome","price":"₹349","mrp":"₹600","img":"https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=400","rating":"4.1"},
    {"cat":"Body","name":"Bonnet Panel","price":"₹5,999","mrp":"₹8,500","img":"https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=400","rating":"4.6"},
    {"cat":"Body","name":"Fender - Left","price":"₹2,199","mrp":"₹3,200","img":"https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=400","rating":"4.2"},
    {"cat":"Body","name":"Tail Light Pair","price":"₹1,799","mrp":"₹2,500","img":"https://images.unsplash.com/photo-1551524559-8af4e6624178?w=400","rating":"4.5"},
    {"cat":"Body","name":"Windshield Glass","price":"₹4,499","mrp":"₹6,500","img":"https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?w=400","rating":"4.7"},
    {"cat":"Body","name":"Roof Carrier","price":"₹2,999","mrp":"₹4,500","img":"https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=400","rating":"4.3"},

    # --- EXTERNAL ACCESSORIES (8) ---
    {"cat":"External","name":"17 Inch Alloy Wheels","price":"₹19,999","mrp":"₹28,000","img":"https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=400","rating":"4.9"},
    {"cat":"External","name":"LED Headlight 200W","price":"₹1,199","mrp":"₹2,000","img":"https://images.unsplash.com/photo-1551524559-8af4e6624178?w=400","rating":"4.6"},
    {"cat":"External","name":"Waterproof Car Cover","price":"₹799","mrp":"₹1,500","img":"https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=400","rating":"4.4"},
    {"cat":"External","name":"Rear Spoiler","price":"₹2,499","mrp":"₹4,000","img":"https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=400","rating":"4.2"},
    {"cat":"External","name":"Mud Flaps Set","price":"₹499","mrp":"₹900","img":"https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=400","rating":"4.0"},
    {"cat":"External","name":"Fog Lights Pair","price":"₹1,499","mrp":"₹2,200","img":"https://images.unsplash.com/photo-1551524559-8af4e6624178?w=400","rating":"4.5"},
    {"cat":"External","name":"Chrome Grill","price":"₹1,899","mrp":"₹2,800","img":"https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=400","rating":"4.3"},
    {"cat":"External","name":"Antenna Shark Fin","price":"₹299","mrp":"₹600","img":"https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=400","rating":"4.1"},

    # --- INTERNAL ACCESSORIES (8) ---
    {"cat":"Internal","name":"Leather Seat Cover","price":"₹3,999","mrp":"₹6,500","img":"https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?w=400","rating":"4.8"},
    {"cat":"Internal","name":"Leather Steering Cover","price":"₹399","mrp":"₹700","img":"https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?w=400","rating":"4.4"},
    {"cat":"Internal","name":"9H Music System Android","price":"₹6,499","mrp":"₹9,999","img":"https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=400","rating":"4.9"},
    {"cat":"Internal","name":"7D Floor Mats","price":"₹1,499","mrp":"₹2,500","img":"https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=400","rating":"4.6"},
    {"cat":"Internal","name":"Dashboard Perfume","price":"₹249","mrp":"₹400","img":"https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?w=400","rating":"4.2"},
    {"cat":"Internal","name":"Mobile Holder","price":"₹199","mrp":"₹399","img":"https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?w=400","rating":"4.3"},
    {"cat":"Internal","name":"Neck Rest Pillow 2pc","price":"₹599","mrp":"₹1,000","img":"https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=400","rating":"4.5"},
    {"cat":"Internal","name":"LED Cabin Lights","price":"₹349","mrp":"₹600","img":"https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=400","rating":"4.4"},
]

page = """
<!DOCTYPE html>
<html><head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AutoParts Hub - Sasta Bazar</title>
<style>
*{box-sizing:border-box} body{margin:0; font-family:system-ui; background:#020617; color:white;}
.header{position:sticky; top:0; background:#0f172a; padding:12px; z-index:10; border-bottom:1px solid #1e293b;}
h1{margin:0; color:#38bdf8; font-size:20px; text-align:center;}
.sub{text-align:center; color:#94a3b8; font-size:12px;}
.search{width:100%; padding:12px 15px; border-radius:12px; border:none; margin-top:10px; background:#1e293b; color:white; font-size:15px;}
.tabs{display:flex; gap:8px; overflow:auto; padding:12px; background:#0f172a; position:sticky; top:88px; z-index:9;}
.tab{padding:8px 16px; background:#1e293b; border-radius:20px; font-size:13px; white-space:nowrap; border:1px solid #334155;}
.tab.active{background:#38bdf8; color:black; font-weight:bold; border-color:#38bdf8;}
.grid{display:grid; grid-template-columns:1fr 1fr; gap:10px; padding:10px;}
.card{background:#1e293b; border-radius:16px; overflow:hidden; border:1px solid #1e293b;}
.card img{width:100%; height:120px; object-fit:cover;}
.info{padding:8px 10px;}
.badge{font-size:9px; background:#334155; padding:3px 7px; border-radius:20px; color:#cbd5e1;}
.name{font-size:13px; font-weight:600; margin:5px 0; height:32px; overflow:hidden;}
.prices{display:flex; gap:6px; align-items:center;}
.price{color:#22c55e; font-weight:bold; font-size:14px;}
.mrp{color:#64748b; font-size:11px; text-decoration:line-through;}
.rating{font-size:11px; color:#facc15; margin-top:2px;}
.btns{display:flex; gap:6px; margin-top:8px;}
.buy{flex:2; background:#38bdf8; border:none; padding:8px; border-radius:8px; font-weight:bold; font-size:12px;}
.cart{flex:1; background:#334155; color:white; border:none; padding:8px; border-radius:8px;}
.cart-bar{position:fixed; bottom:0; left:0; right:0; background:#0f172a; border-top:1px solid #1e293b; padding:12px; display:flex; justify-content:space-between; align-items:center;}
</style>
</head><body>
<div class="header">
<h1>🚗 AutoParts Hub Jharkhand</h1>
<div class="sub">32 Products | Saste Daam | All india FREE Delivery</div>
<input class="search" id="s" onkeyup="searchP()" placeholder="🔍 Search - jaise brake, oil, light...">
</div>

<div class="tabs">
<div class="tab active" onclick="filterC('All',this)">All 32</div>
<div class="tab" onclick="filterC('Engine',this)">🔧 Engine (8)</div>
<div class="tab" onclick="filterC('Body',this)">🚘 Body (8)</div>
<div class="tab" onclick="filterC('External',this)">✨ External (8)</div>
<div class="tab" onclick="filterC('Internal',this)">💺 Internal (8)</div>
</div>

<div class="grid" id="list">PRODUCTS</div>

<div style="height:80px"></div>
<div class="cart-bar">
<span>🛒 Cart: <b id="count">0</b> items</span>
<span style="color:#22c55e" id="total">Total: ₹0</span>
</div>

<script>
let c=0, t=0;
function filterC(cat,el){
 document.querySelectorAll('.tab').forEach(x=>x.classList.remove('active')); el.classList.add('active');
 document.querySelectorAll('.card').forEach(x=>{ x.style.display = (cat=='All' || x.dataset.cat==cat)?'block':'none'; });
}
function searchP(){
 let v=document.getElementById('s').value.toLowerCase();
 document.querySelectorAll('.card').forEach(x=>{ x.style.display = x.innerText.toLowerCase().includes(v)?'block':'none'; });
}
function add(p,pr){
 c++; t+=parseInt(pr.replace(/[^0-9]/g,''));
 document.getElementById('count').innerText=c;
 document.getElementById('total').innerText='Total: ₹'+t;
 alert(p+' Add ho gaya! Cart me '+c+' items');
}
</script>
</body></html>
"""

cards_html=""
for pr in products:
    cards_html+=f"""<div class="card" data-cat="{pr['cat']}"><img src="{pr['img']}"><div class="info"><span class="badge">{pr['cat']}</span><div class="name">{pr['name']}</div><div class="rating">⭐ {pr['rating']} | 120+ Sold</div><div class="prices"><span class="price">{pr['price']}</span><span class="mrp">{pr['mrp']}</span></div><div class="btns"><button class="buy" onclick="add('{pr['name']}','{pr['price']}')">BUY NOW</button><button class="cart" onclick="add('{pr['name']}','{pr['price']}')">+🛒</button></div></div></div>"""

@app.route('/')
def home():
    return page.replace("PRODUCTS", cards_html)

if __name__  == '__main__' :
    print("Server chalu... Pydroid ke upar link pe click kar")
app.run(host='0.0.0.0', port=5000)
