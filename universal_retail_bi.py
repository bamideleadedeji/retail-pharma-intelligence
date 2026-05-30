import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os

# --- ARCHITECTURAL SETUP ---
st.set_page_config(page_title="UniversalIntelligence AI | Retail & Pharma", layout="wide", page_icon="💊")

# Premium Corporate Dark FinTech Styling
st.markdown("""
    <style>
    .main { background-color: #0d1117; }
    div[data-testid="stMetricValue"] { font-size: 30px; color: #00ff88; font-weight: 700; }
    .stDataFrame { border: 1px solid #30363d; border-radius: 8px; }
    [data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #30363d; }
    h1, h2, h3, h4 { color: #f0f6fc; font-weight: 600; }
    .stAlert { background-color: #1f1f2e; border-left: 5px solid #00ff88; }
    </style>
    """, unsafe_allow_html=True)

# --- SIMULATED REAL-TIME HYBRID DATA ENGINE ---
@st.cache_data(ttl=60)
def generate_universal_live_stream():
    """Generates a high-fidelity data matrix modeling a unified Nigerian Grocery & Pharmacy pipeline."""
    np.random.seed(100)
    n_rows = 1500
    
    universal_catalog = {
        'FMCG / Provisions': ['Peak Milk 400g', 'Milo 400g', 'Three Crowns 380g', 'Dano Milk Refill'],
        'Grains & Staples': ['Mama Gold Rice 10kg', 'Honeywell Flour 1kg', 'Golden Penny Spaghetti', 'Dangote Sugar 1kg'],
        'Beverages & Chillers': ['Coca-Cola 50cl', 'Eva Water 75cl', 'Malta Guinness 33cl', 'Hollandia Yoghurt 1L'],
        'Toiletries & Homecare': ['Dettol Soap Cool', 'Hypo Bleach Super', 'Ariel Detergent 400g', 'Sunlight Dishwash'],
        'Pharmacy / OTC Drugs': ['Emzor Paracetamol Pack', 'Panadol Extra', 'Procold Tablet', 'Amoxil 500mg Capsule'],
        'Pharmacy / Supplements': ['Nature Field Vitamin C 1000mg', 'Cod Liver Oil Caps', 'Astymin Syrup', 'Wellman Premium']
    }
    
    flat_products, categories = [], []
    for cat, prods in universal_catalog.items():
        for p in prods:
            flat_products.append(p)
            categories.append(cat)
            
    prod_pool = np.random.choice(len(flat_products), n_rows)
    dates = pd.date_range(start='2026-05-01', end='2026-05-30', periods=n_rows)
    qty = np.random.randint(1, 15, size=n_rows)
    
    data = []
    for i in range(n_rows):
        p_idx = prod_pool[i]
        p_cat = categories[p_idx]
        
        # Apply structural pricing logic based on category risk profile
        if 'Pharmacy' in p_cat:
            cp = round(np.random.uniform(1200, 8500), 2)
            markup = np.random.uniform(1.25, 1.45) # Higher margin structure
        else:
            cp = round(np.random.uniform(600, 5000), 2)
            markup = np.random.uniform(1.10, 1.22) # Fast moving, thin margins
            
        sp = round(cp * markup, 2)
        units_sold = qty[i]
        
        data.append({
            'Timestamp': dates[i],
            'Category': p_cat,
            'Product_Name': flat_products[p_idx],
            'Cost_Price': cp,
            'Selling_Price': sp,
            'Quantity_Sold': units_sold,
            'Revenue': round(sp * units_sold, 2),
            'Cost_of_Goods': round(cp * units_sold, 2),
            'Gross_Profit': round((sp - cp) * units_sold, 2),
            'Current_Stock_Level': np.random.randint(0, 200),
            'Reorder_Level': 40
        })
    return pd.DataFrame(data)

# --- PLATFORM INITIALIZATION ---
df_raw = generate_universal_live_stream()

st.sidebar.title("🛡️ UniversalIntelligence")
st.sidebar.caption("Hybrid Retail Middleware Engine v2.0")
st.sidebar.markdown("---")

store_module = st.sidebar.radio("Executive Portals", ["CEO Financial Monitor", "Pharma & Grocery Inflow Guard"])

# --- MODULE 1: CEO FINANCIAL MONITOR ---
if store_module == "CEO Financial Monitor":
    st.title("Enterprise Hybrid Hub | Executive Portfolio Dashboard")
    st.caption("Unified Analysis of Consolidated Pharmacy Assets and Fast-Moving Grocery Streams")
    st.markdown("---")
    
    total_rev = df_raw['Revenue'].sum()
    total_cogs = df_raw['Cost_of_Goods'].sum()
    total_profit = df_raw['Gross_Profit'].sum()
    avg_margin = (total_profit / total_rev) * 100
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Unified Gross Revenue", f"₦{total_rev:,.2f}")
    m2.metric("Portfolio Cost (COGS)", f"₦{total_cogs:,.2f}")
    m3.metric("Net Gross Profit Pool", f"₦{total_profit:,.2f}")
    m4.metric("Blended Profit Margin", f"{avg_margin:.2f}%")
    st.markdown("---")
    
    c_left, c_right = st.columns([2, 1])
    with c_left:
        st.subheader("Temporal Yield Optimization Curve")
        daily_perf = df_raw.groupby(df_raw['Timestamp'].dt.date)[['Revenue', 'Gross_Profit']].sum().reset_index()
        fig_line = px.line(daily_perf, x='Timestamp', y=['Revenue', 'Gross_Profit'], 
                           template="plotly_dark", color_discrete_sequence=['#00ff88', '#ffaa00'])
        fig_line.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', xaxis_title="Operational Timeline", yaxis_title="Value (₦)")
        st.plotly_chart(fig_line, use_container_width=True)
        
    with c_right:
        st.subheader("Margin Contribution Map")
        cat_perf = df_raw.groupby('Category')['Gross_Profit'].sum().reset_index()
        fig_pie = px.pie(cat_perf, names='Category', values='Gross_Profit', hole=0.4,
                         color_discrete_sequence=px.colors.sequential.Greens_r)
        fig_pie.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_pie, use_container_width=True)

# --- MODULE 2: PHARMA & GROCERY INFLOW GUARD ---
elif store_module == "Pharma & Grocery Inflow Guard":
    st.title("Replenishment Logistics & Stock-Out Prevention Engine")
    st.caption("Automated threshold triggers tracking shelf drain rates for medicinal and household items.")
    st.markdown("---")
    
    # Critical Threshold Alert Filters
    st.subheader("🚨 Universal Reorder Warnings")
    alert_df = df_raw[df_raw['Current_Stock_Level'] <= df_raw['Reorder_Level']].copy()
    alert_summary = alert_df.groupby(['Category', 'Product_Name', 'Current_Stock_Level', 'Reorder_Level']).size().reset_index()
    alert_summary['Required_Restock_Units'] = 150 - alert_summary['Current_Stock_Level']
    
    # Highlight completely empty shelves (Stock level = 0)
    critical_stockouts = alert_summary[alert_summary['Current_Stock_Level'] == 0]
    if not critical_stockouts.empty:
        st.error(f"🔴 CRITICAL REVENUE RISK: Exactly {len(critical_stockouts)} essential items are COMPLETELY OUT OF STOCK on the shelves. Re-order immediately.")
    
    if not alert_summary.empty:
        st.dataframe(alert_summary[['Category', 'Product_Name', 'Current_Stock_Level', 'Reorder_Level', 'Required_Restock_Units']].style.format({
            "Current_Stock_Level": "{:,.0f} units left",
            "Reorder_Level": "Threshold: {:,.0f}",
            "Required_Restock_Units": "+{:,.0f} units Order Target"
        }), use_container_width=True)
    else:
        st.success("All stock indices are operating within safe storage parameters.")
        
    st.markdown("---")
    
    # Velocity Indexing
    st.subheader(" Absolute Velocity Index (Cross-Department Performance)")
    velocity_df = df_raw.groupby(['Category', 'Product_Name'])['Quantity_Sold'].sum().reset_index()
    velocity_df = velocity_df.sort_values(by='Quantity_Sold', ascending=False).reset_index(drop=True)
    
    st.dataframe(velocity_df.style.format({"Quantity_Sold": "{:,.0f} items distributed MTD"}), use_container_width=True)
