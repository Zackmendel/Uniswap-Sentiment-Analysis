import json
from datetime import datetime
from urllib.request import Request, urlopen

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import streamlit_antd_components as sac
from pandas import json_normalize
from plotly.subplots import make_subplots
from streamlit.components.v1 import html

st.set_page_config(layout="wide")

# Create a session state to store the selected menu item
# session_state = st.session_state
# if "selected_menu_item" not in session_state:
#     session_state.selected_menu_item = None

with st.sidebar:
  st.image("https://static.vecteezy.com/system/resources/previews/011/307/370/non_2x/uniswap-uni-badge-crypto-3d-rendering-free-png.png")

  selected_menu_items = sac.menu([
      sac.MenuItem('Home', icon='house-fill'),
      sac.MenuItem('Fundamental Analysis', icon='box-fill'),
      sac.MenuItem('Technical Analysis', icon='git',),
      sac.MenuItem('Greed & Fear Index', icon='google')
      # sac.MenuItem('Useful Widgets', icon='Widgets')
      ])

  # ], format_func='title', open_all=True)

#     # Check if a menu item is selected
#     if selected_menu_items and len(selected_menu_items) > 0:
#         session_state.selected_menu_item = selected_menu_items[0]

# # Print the selected menu item
# if session_state.selected_menu_item:
#     st.header(f"Selected Menu Item: {session_state.selected_menu_item}")




# ____________________________________________________________________________________________________________________________________________________________________________


if selected_menu_items == 'Home':
  col_a, col_b, col_c = st.columns([1,3,1])
  with col_a:
    st.image("https://static.vecteezy.com/system/resources/previews/011/307/370/non_2x/uniswap-uni-badge-crypto-3d-rendering-free-png.png")

  # with col_b:
  #   sac.divider(label='-',  align='center')
  #   st.subheader("Important Sources:")
  #   sac.divider(label='--', align='center')

  with col_b:
    sac.divider(label='.',  align='center')
    sac.divider(label='..',  align='center')
    sac.buttons([
        sac.ButtonsItem(label='Important Sources:'),
        sac.ButtonsItem(label='Flipsidecrypto', href='https://flipsidecrypto.xyz'),
        sac.ButtonsItem(label='Alternative.me', href='https://alternative.me'),
        sac.ButtonsItem(label='Coinstats', href='https://coinstats.app'),
        sac.ButtonsItem(label='TradingView', href='https://tradingview.com'),
    ], format_func='title', align='center')
  
    #DIVIDER
    # sac.divider(label='....', align='center')

  with col_c:
    st.image("https://static.vecteezy.com/system/resources/previews/011/307/370/non_2x/uniswap-uni-badge-crypto-3d-rendering-free-png.png")

  
  st.markdown(f'<h1 style="background-image:url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR161CeyquZeVivKqosn-o7etI4ca0CG8kIexNzsB3BGmkE0CfrA_n8epPfyU7n5bZZz3E&usqp=CAU);font-weight:bold;font-family:Georgia;font-size:60px;text-align:center;text-shadow: 5px 5px black;color:#f23a7d;box-shadow: 3px 3px black;">{"Market sentiment on Uniswap"}</h1>', unsafe_allow_html=True)
  
  # st.markdown(f'<h1 style="font-weight:bold;font-family:Georgia;font-size:60px;text-align:center;text-shadow: 5px 5px black;color:#f23a7d;">{"Market sentiment on Uniswap"}</h1>', unsafe_allow_html=True)

  st.markdown(f'<h1 style="font-weight:bold;font-family:Georgia;font-size:30px;text-align:left;text-shadow: 5px 5px black;color:#f23a7d;">{"Introduction:"}</h1>', unsafe_allow_html=True)

  st.markdown("""
  In the dynamic realm of cryptocurrency, market sentiment plays a pivotal role in influencing various metrics, including trading volumes, user activity, and Total Value Locked (TVL). As the crypto landscape evolves rapidly, market participants eagerly await regulatory decisions that could shape the trajectory of the market. The imminent decision on SEC approval for a spot Bitcoin ETF adds a layer of anticipation and uncertainty to the current landscape.

  The question at the forefront of analysis is how market sentiment, influenced by factors such as SEC decisions, historical market trends, and user behavior, can offer insights into potential future market movements. In response to this inquiry, a comprehensive market sentiment dashboard has been created. This dashboard delves into historical data from both bull and bear markets, exploring indicators that may provide clues about the future direction of the crypto market.
  """)

  st.markdown(f'<h1 style="font-weight:bold;font-family:Georgia;font-size:30px;text-align:center;text-shadow: 5px 5px black;color:#f23a7d;">{"KEY FINDINGS🔎:"}</h1>', unsafe_allow_html=True)

  ### Fundamental Analysis
  st.markdown(f'<h1 style="font-weight:bold;font-family:Georgia;font-size:30px;text-align:left;text-shadow: 5px 5px black;color:#f23a7d;">{"Fundamental Analysis:"}</h1>', unsafe_allow_html=True)

  st.markdown("""
  The fundamental analysis begins by scrutinizing various metrics related to volume, encompassing the crypto market cap, trading volumes on centralized and decentralized exchanges, and moving averages. The total crypto market cap, as depicted in historical data, highlights the market's attempt to regain momentum since its peak in 2021. The current market cap, lagging by 1 trillion USD, is poised delicately, awaiting the outcome of SEC approval.

  Daily trading volumes on decentralized exchanges (DEXes) showcase a steady range until late October, followed by a doubling trend, indicating potential market shifts. User visitation on DEXes, reaching an all-time high, aligns with short-term bullish signals but prompts caution regarding sustainability.
  """)

  ### Technical Analysis
  st.markdown(f'<h1 style="font-weight:bold;font-family:Georgia;font-size:30px;text-align:left;text-shadow: 5px 5px black;color:#f23a7d;">{"Technical Analysis:"}</h1>', unsafe_allow_html=True)

  st.markdown("""

  The technical analysis focuses on three key tokens: Bitcoin (BTC), Ethereum (ETH), and Uniswap (UNI). These tokens serve as case studies to predict overall market trends. Notably, the upward trend in moving averages signals a bullish market, with potential implications for short and long-term trends. BTC's significant drop on January 3, 2024, attributed to nervous market dynamics, underscores the impact of market sentiment on token prices.
  """)

  ### Greed and Fear Index
  st.markdown(f'<h1 style="font-weight:bold;font-family:Georgia;font-size:30px;text-align:left;text-shadow: 5px 5px black;color:#f23a7d;">{"Greed and Fear Index:"}</h1>', unsafe_allow_html=True)

  st.markdown("""
  The Greed and Fear Index, a tool gauging market sentiment, currently stands at 68, indicating a state of greed. The index considers factors like volatility, market momentum, social media engagement, surveys, and dominance. An extended period of greed, spanning close to three months, raises questions about a potential bearish run. However, the impending SEC approval introduces an element of unpredictability, potentially fueling further bullish momentum.
  """)

  # Conclusion:
  st.markdown(f'<h1 style="font-weight:bold;font-family:Georgia;font-size:30px;text-align:center;text-shadow: 5px 5px black;color:#f23a7d;">{"CONCLUSION:"}</h1>', unsafe_allow_html=True)
  
  st.markdown("""
  As the crypto market braces for the SEC's decision on spot Bitcoin ETFs, the market sentiment dashboard provides a multifaceted view of historical trends, technical indicators, and the psychological aspects reflected in the Greed and Fear Index. While indicators suggest potential bullish movements, the delicate balance and the looming regulatory decision introduce an element of uncertainty. The crypto community must navigate these intricate dynamics, considering the interplay of market sentiment and regulatory outcomes in shaping the future trajectory of the cryptocurrency landscape.
  """)




# ____________________________________________________________________________________________________________________________________________________________________________
  

elif selected_menu_items == 'Fundamental Analysis':
  st.markdown(f'<h1 style="font-weight:bold;font-family:Georgia;font-size:60px;text-align:center;text-shadow: 5px 5px black;color:#f23a7d;">{"Fundamental Analysis"}</h1>', unsafe_allow_html=True)

  st.markdown("""
  Here, we are going to be looking at metrics related to volume, including the size of the crypto market cap, trading volume, buying and selling in CEXes and DEXes, moving averages of the volume, among others.

Monitoring these metrics will give us a general overview of what is going on in the crypto market currently and provide us with an in-depth understanding of the trends that can be expected in future times.

The chart below represents the total crypto market cap as provided by [TradingView](https://www.tradingview.com/widget/symbol-overview/). From the historical data, it can be seen that since the crypto market cap peaked in 2021, the crypto market has been attempting to regain that same momentum over time. With the crypto cap currently around 1.6T USD, it is still lagging behind the peak value by 1T USD.

Owing to whether the SEC approval is favorable or not, the possibilities of attaining the previous peak values are hanging by a thin thread.

  """)

  # col_a, col_b = st.columns([3,1])
  # with col_a:

  st.markdown(f'<h1 style="font-weight:bold;font-family:Georgia;font-size:30px;text-align:center;text-shadow: 5px 5px black;color:#f23a7d;">{"Crypto Market Cap"}</h1>', unsafe_allow_html=True)
  
  # st.subheader("")

  trading_view = """<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/" rel="noopener nofollow" target="_blank"><span class="blue-text">Track all markets on TradingView</span></a></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-overview.js" async>
  {
  "symbols": [
    [
      "CRYPTOCAP:TOTAL|ALL"
    ]
  ],
  "chartOnly": false,
  "width": "1000",
  "height": "500",
  "locale": "en",
  "colorTheme": "dark",
  "autosize": true,
  "showVolume": true,
  "showMA": true,
  "hideDateRanges": false,
  "hideMarketStatus": false,
  "hideSymbolLogo": false,
  "scalePosition": "right",
  "scaleMode": "Normal",
  "fontFamily": "-apple-system, BlinkMacSystemFont, Trebuchet MS, Roboto, Ubuntu, sans-serif",
  "fontSize": "10",
  "noTimeScale": false,
  "valuesTracking": "1",
  "changeMode": "price-and-percent",
  "chartType": "area",
  "maLineColor": "#2962FF",
  "maLineWidth": 1,
  "maLength": 9,
  "lineWidth": 2,
  "lineType": 0,
  "dateRanges": [
    "1d|1",
    "1m|30",
    "3m|60",
    "12m|1D",
    "60m|1W",
    "all|1M"
  ],
  "timeHoursFormat": "12-hours"
}
  </script>
</div>
<!-- TradingView Widget END -->"""

  html(trading_view, height=500) #, width=220)

  st.write("SOURCE:[TradingView](https://www.tradingview.com/widget/symbol-overview/)")



  
  st.markdown(f'<h1 style="font-weight:bold;font-family:Georgia;font-size:30px;text-align:center;text-shadow: 5px 5px black;color:#f23a7d;">{"DEX Trading Volume Vs Moving Averages(20, 50 and 200 days)"}</h1>', unsafe_allow_html=True)


  # Sample data
  url = 'https://flipsidecrypto.xyz/api/v1/queries/dc27d475-6e02-4b73-9649-85155888fbf2/data/latest'
  req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
  response = urlopen(req).read()
  data = response.decode('utf-8')
  df2 = pd.read_json(data)

  col_a, col_b = st.columns([3,1])
  with col_a:

    # Create subplots
    fig1a = make_subplots(specs=[[{"secondary_y": True}]])
  
    # Add scatter plot for Volume
    fig1a.add_trace(
        go.Scatter(
            x=df2['TIMESPAN'],
            y=df2['VOLUME'],
            name="Volume",
            mode="lines",
            marker_color='mintcream'
        ),
        secondary_y=True
    )
  
    # Add scatter plot for MOV_AG_20DAYS
    fig1a.add_trace(
        go.Scatter(
            x=df2['TIMESPAN'],
            y=df2['MOV_AG_20DAYS'],
            name="MA_20",
            mode="lines",
            marker_color='blue'
        ),
        secondary_y=False
    )
  
    # Add scatter plot for MOV_AVG_50DAYS
    fig1a.add_trace(
        go.Scatter(
            x=df2['TIMESPAN'],
            y=df2['MOV_AVG_50DAYS'],
            name="MA_50",
            mode="lines",
            marker_color='yellow'
        ),
        secondary_y=False
    )
  
    # Add scatter plot for MOV_AVG_200DAYS
    fig1a.add_trace(
        go.Scatter(
            x=df2['TIMESPAN'],
            y=df2['MOV_AVG_200DAYS'],
            name="MA_200",
            mode="lines",
            marker_color='red'
        ),
        secondary_y=False
    )
  
    
    # Update x-axis title
    fig1a.update_xaxes(title_text="Timespan")
  
    # Set y-axes titles
    fig1a.update_yaxes(title_text="Moving Averages (MA)", secondary_y=False)
    fig1a.update_yaxes(title_text="Volume", secondary_y=True)
  
    # Show the plot
    st.plotly_chart(fig1a, use_container_width=True)

    st.write("SOURCE:[Flipsidecrypto](https://flipsidecrypto.xyz/edit/queries/dc27d475-6e02-4b73-9649-85155888fbf2)")
    

  with col_b:
    st.markdown("""
    From the daily trading volume of decentralized exchanges (DEXes), it can be seen that the daily trading volume over time has been in a steady range of around 1-2 billion dollars until late October when the value doubled to range from around 2-4 billion dollars and has been in an upward trend since then.

The moving averages were also pointing towards a bearish trend until the above date when they all crossed each other and went upwards, indicating a bullish run. The fact that the 20 & 50 days MAs are very steep and above the 200 days MA indicates a short bullish trend and is possible to come crashing down.
    """)


  st.markdown(f'<h1 style="font-weight:bold;font-family:Georgia;font-size:30px;text-align:center;text-shadow: 5px 5px black;color:#f23a7d;">{"DEX Trading Transactions(Swaps) Vs Moving Averages(20, 50 and 200 days)"}</h1>', unsafe_allow_html=True)

  col_c, col_d = st.columns([3,1])
  with col_c:
    req = Request('https://flipsidecrypto.xyz/api/v1/queries/7f29a794-79fb-42dd-ad7f-69ce3bad13eb/data/latest', headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req).read()
    data = response.decode('utf-8')
    df3 = pd.read_json(data)
  
    # with col2:
    figb = px.line(df3, x="TIMESPAN", y="TRANSACTIONS", title="Daily Trading Transactions(Swaps) of Dexes", height=500)
    figb.update_layout(hovermode="x unified")
    figb.add_scatter(x=df3['TIMESPAN'], y=df3['MOV_AG_20DAYS'], name='MA_20')
    figb.add_scatter(x=df3['TIMESPAN'], y=df3['MOV_AVG_50DAYS'], name='MA_50')
    figb.add_scatter(x=df3['TIMESPAN'], y=df3['MOV_AVG_200DAYS'], name='MA_200')
    st.plotly_chart(figb, use_container_width=True)

    st.write("SOURCE:[Flipsidecrypto](https://flipsidecrypto.xyz/edit/queries/7f29a794-79fb-42dd-ad7f-69ce3bad13eb)")


  with col_d:
    st.markdown("""
  .
  
  .
  
  The same can be noticed with the user visitation or usage of decentralized exchanges, with them recording an all-time high since the past year of about 4 million transactions in a day in contrast with the 1 million transactions per day recorded throughout the year. This is also a short-term bullish signal and can be seen that it might not be sustainable over a long period of time.
  """)
  


  # st.image("https://alternative.me/crypto/fear-and-greed-index.png")
  


  # st.dataframe(
  #   df,
  # column_config={
  #   "circulating_supply": st.column_config.ProgressColumn(
  #       "Circulating Supply",
  #       help="The sales volume in USD",
  #       format="$%d",
  #       min_value=0,
  #       max_value=100000000000,
  #   ),
  # },
  # hide_index=True,
  # )
  # st.dataframe(df.style.highlight_max(axis=2))


# ____________________________________________________________________________________________________________________________________________________________________________



elif selected_menu_items == 'Technical Analysis':
  st.markdown(f'<h1 style="font-weight:bold;font-family:Georgia;font-size:60px;text-align:center;text-shadow: 5px 5px black;color:#f23a7d;">{"Technical Analysis"}</h1>', unsafe_allow_html=True)
  # st.subheader("Technical Analysis")

  st.markdown("""
  The price of tokens in the past speaks volumes of their behavior in the future. In this segment, we shall be putting our lens on three(3) tokens in order to predict the overall market trend in times to come.

Bitcoin (BTC), as the major driver of the cryptocurrency space, will be used as the primary case study to observe the market trend. As can be seen from the price chart below, the price has been in an upward trend pending SEC approval slated for early January. Also, BTC experienced a significant drop in its price on the 3rd of January 2024. This drop can be attributed to nervousness on the part of holders and investors, causing selling rates to soar and buying rates to plummet. We shall delve into these details in the later sections.

Ethereum (ETH), the second leading token and blockchain in the crypto-verse, will be our second case study. Interestingly, its price trend is similar to that of BTC, and inferences drawn from BTC can also be related to that of ETH.

Uniswap (UNI), the governance token of the leading decentralized exchange, is then considered to see if BTC truly affects the general market movement of tokens in the crypto-verse.

### Let's go 💪😀🏃‍♂️👉👉

  """)

  marquee_widget = """
    <script defer src="https://www.livecoinwatch.com/static/lcw-widget.js"></script> <div class="livecoinwatch-widget-5" lcw-base="USD" lcw-color-tx="#ffffff" lcw-marquee-1="coins" lcw-marquee-2="movers" lcw-marquee-items="30" ></div>
    """

  html(marquee_widget)#, height=70, width=220)

  st.write("SOURCE:[Livecoinwatch.com](https://www.livecoinwatch.com/widgets)")
  

  st.markdown(f'<h1 style="font-weight:bold;font-family:Georgia;font-size:30px;text-align:center;text-shadow: 5px 5px black;color:#f23a7d;">{"Seven(7) Days Price of BTC, ETH & UNI"}</h1>', unsafe_allow_html=True)

  cola, colb, colc = st.columns([1,1,1])
  with cola:
    btc_price = """
    <script defer src="https://www.livecoinwatch.com/static/lcw-widget.js"></script> <div class="livecoinwatch-widget-1" lcw-coin="BTC" lcw-base="USD" lcw-secondary="ETH" lcw-period="w" lcw-color-tx="#ffffff" lcw-color-pr="#fcb900" lcw-color-bg="#1f2434" lcw-border-w="1" ></div>
    """
    html(btc_price, height=230)#, width=220)
    st.markdown("""
    
    """)

  with colb:
    eth_price = """
    <script defer src="https://www.livecoinwatch.com/static/lcw-widget.js"></script> <div class="livecoinwatch-widget-1" lcw-coin="ETH" lcw-base="USD" lcw-secondary="BTC" lcw-period="w" lcw-color-tx="#ffffff" lcw-color-pr="#8ed1fc" lcw-color-bg="#0a3058" lcw-border-w="1" ></div>
    """
    html(eth_price, height=230)#, width=220)

  with colc:
    uni_price = """
    <script defer src="https://www.livecoinwatch.com/static/lcw-widget.js"></script> <div class="livecoinwatch-widget-1" lcw-coin="UNI" lcw-base="USD" lcw-secondary="BTC" lcw-period="w" lcw-color-tx="#ffffff" lcw-color-pr="#abb8c3" lcw-color-bg="#471024" lcw-border-w="1" ></div>
    """
    html(uni_price, height=230)#, width=220)

  st.write("SOURCE:[Livecoinwatch.com](https://www.livecoinwatch.com/widgets)")

  st.markdown(f'<h1 style="font-weight:bold;font-family:Georgia;font-size:30px;text-align:center;text-shadow: 5px 5px black;color:#f23a7d;">{"Short & Long Term Moving Averages of BTC, ETH & UNI"}</h1>', unsafe_allow_html=True)


  # Sample data
  url = 'https://flipsidecrypto.xyz/api/v1/queries/987bba9c-9885-498f-bb3e-026a0fe7abb8/data/latest'
  req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
  response = urlopen(req).read()
  data = response.decode('utf-8')
  df2 = pd.read_json(data)

  # Get unique tokens for dropdown menu
  token_options = ('BTC', 'ETH', 'UNI')

  # Dropdown for token selection
  selected_token = st.selectbox("Select Token", token_options)

  # Filter df1 based on selected token
  df1 = df2[df2['TOKEN'] == selected_token]

  if selected_token == 'BTC':
    col_d, col_e = st.columns(2)
    with col_d:
      st.subheader('SHORT TERM MOVING AVERAGE')
  
      # Create subplots
      fig1a = make_subplots(specs=[[{"secondary_y": True}]])
  
      # Add scatter plot for Volume
      fig1a.add_trace(
          go.Scatter(
              x=df2['TIMESPAN'],
              y=df2['PRICE_USD'],
              name="Price",
              mode="lines",
              marker_color='mintcream'
          ),
          secondary_y=True
      )
  
      # Add scatter plot for MOV_AG_20DAYS
      fig1a.add_trace(
          go.Scatter(
              x=df2['TIMESPAN'],
              y=df2['MOV_AG_20DAYS'],
              name="MA_20",
              mode="lines",
              marker_color='blue'
          ),
          secondary_y=False
      )
  
      # Add scatter plot for MOV_AVG_50DAYS
      fig1a.add_trace(
          go.Scatter(
              x=df2['TIMESPAN'],
              y=df2['MOV_AVG_50DAYS'],
              name="MA_50",
              mode="lines",
              marker_color='yellow'
          ),
          secondary_y=False
      )
  
      # Update x-axis title
      fig1a.update_xaxes(title_text="Timespan")
  
      # Set y-axes titles
      fig1a.update_yaxes(title_text="Moving Averages (MA)", secondary_y=False)
      fig1a.update_yaxes(title_text="PRICE(USD)", secondary_y=True)
  
      # Show the plot
      st.plotly_chart(fig1a, use_container_width=True)
  
  
    with col_e:
      st.subheader('LONG TERM MOVING AVERAGE')
  
      # Create subplots
      fig1a = make_subplots(specs=[[{"secondary_y": True}]])
  
      # Add scatter plot for Volume
      fig1a.add_trace(
          go.Scatter(
              x=df2['TIMESPAN'],
              y=df2['PRICE_USD'],
              name="Price",
              mode="lines",
              marker_color='mintcream'
          ),
          secondary_y=True
      )
  
      # Add scatter plot for MOV_AVG_50DAYS
      fig1a.add_trace(
          go.Scatter(
              x=df2['TIMESPAN'],
              y=df2['MOV_AVG_50DAYS'],
              name="MA_50",
              mode="lines",
              marker_color='yellow'
          ),
          secondary_y=False
      )
  
      # Add scatter plot for MOV_AVG_200DAYS
      fig1a.add_trace(
          go.Scatter(
              x=df2['TIMESPAN'],
              y=df2['MOV_AVG_200DAYS'],
              name="MA_200",
              mode="lines",
              marker_color='red'
          ),
          secondary_y=False
      )
  
  
      # Update x-axis title
      fig1a.update_xaxes(title_text="Timespan")
  
      # Set y-axes titles
      fig1a.update_yaxes(title_text="Moving Averages (MA)", secondary_y=False)
      fig1a.update_yaxes(title_text="PRICE(USD)", secondary_y=True)
  
      # Show the plot
      st.plotly_chart(fig1a, use_container_width=True) 

  elif selected_token == 'ETH':
  
  # Sample data
    url = 'https://flipsidecrypto.xyz/api/v1/queries/674cf621-498d-4552-b1ac-c4e4444d4852/data/latest'
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req).read()
    data = response.decode('utf-8')
    df3 = pd.read_json(data)
  
    
    col_d, col_e = st.columns(2)
    with col_d:
      st.subheader('SHORT TERM MOVING AVERAGE')
  
      # Create subplots
      fig1a = make_subplots(specs=[[{"secondary_y": True}]])
  
      # Add scatter plot for Volume
      fig1a.add_trace(
          go.Scatter(
              x=df3['TIMESPAN'],
              y=df3['PRICE_USD'],
              name="Price",
              mode="lines",
              marker_color='mintcream'
          ),
          secondary_y=True
      )
  
      # Add scatter plot for MOV_AG_20DAYS
      fig1a.add_trace(
          go.Scatter(
              x=df3['TIMESPAN'],
              y=df3['MOV_AG_20DAYS'],
              name="MA_20",
              mode="lines",
              marker_color='blue'
          ),
          secondary_y=False
      )
  
      # Add scatter plot for MOV_AVG_50DAYS
      fig1a.add_trace(
          go.Scatter(
              x=df3['TIMESPAN'],
              y=df3['MOV_AVG_50DAYS'],
              name="MA_50",
              mode="lines",
              marker_color='yellow'
          ),
          secondary_y=False
      )
  
      # Update x-axis title
      fig1a.update_xaxes(title_text="Timespan")
  
      # Set y-axes titles
      fig1a.update_yaxes(title_text="Moving Averages (MA)", secondary_y=False)
      fig1a.update_yaxes(title_text="PRICE(USD)", secondary_y=True)
  
      # Show the plot
      st.plotly_chart(fig1a, use_container_width=True)
  
  
    with col_e:
      st.subheader('LONG TERM MOVING AVERAGE')
  
      # Create subplots
      fig1a = make_subplots(specs=[[{"secondary_y": True}]])
  
      # Add scatter plot for Volume
      fig1a.add_trace(
          go.Scatter(
              x=df3['TIMESPAN'],
              y=df3['PRICE_USD'],
              name="Price",
              mode="lines",
              marker_color='mintcream'
          ),
          secondary_y=True
      )
  
      # Add scatter plot for MOV_AVG_50DAYS
      fig1a.add_trace(
          go.Scatter(
              x=df3['TIMESPAN'],
              y=df3['MOV_AVG_50DAYS'],
              name="MA_50",
              mode="lines",
              marker_color='yellow'
          ),
          secondary_y=False
      )
  
      # Add scatter plot for MOV_AVG_200DAYS
      fig1a.add_trace(
          go.Scatter(
              x=df3['TIMESPAN'],
              y=df3['MOV_AVG_200DAYS'],
              name="MA_200",
              mode="lines",
              marker_color='red'
          ),
          secondary_y=False
      )
  
  
      # Update x-axis title
      fig1a.update_xaxes(title_text="Timespan")
  
      # Set y-axes titles
      fig1a.update_yaxes(title_text="Moving Averages (MA)", secondary_y=False)
      fig1a.update_yaxes(title_text="PRICE(USD)", secondary_y=True)
  
      # Show the plot
      st.plotly_chart(fig1a, use_container_width=True) 

  elif selected_token == 'UNI':

  # Sample data
    url = 'https://flipsidecrypto.xyz/api/v1/queries/48993d66-c254-4602-b9ec-1aec9b0dfb05/data/latest'
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req).read()
    data = response.decode('utf-8')
    df3 = pd.read_json(data)


    col_d, col_e = st.columns(2)
    with col_d:
      st.subheader('SHORT TERM MOVING AVERAGE')

      # Create subplots
      fig1a = make_subplots(specs=[[{"secondary_y": True}]])

      # Add scatter plot for Volume
      fig1a.add_trace(
          go.Scatter(
              x=df3['TIMESPAN'],
              y=df3['PRICE_USD'],
              name="Price",
              mode="lines",
              marker_color='mintcream'
          ),
          secondary_y=True
      )

      # Add scatter plot for MOV_AG_20DAYS
      fig1a.add_trace(
          go.Scatter(
              x=df3['TIMESPAN'],
              y=df3['MOV_AG_20DAYS'],
              name="MA_20",
              mode="lines",
              marker_color='blue'
          ),
          secondary_y=False
      )

      # Add scatter plot for MOV_AVG_50DAYS
      fig1a.add_trace(
          go.Scatter(
              x=df3['TIMESPAN'],
              y=df3['MOV_AVG_50DAYS'],
              name="MA_50",
              mode="lines",
              marker_color='yellow'
          ),
          secondary_y=False
      )

      # Update x-axis title
      fig1a.update_xaxes(title_text="Timespan")

      # Set y-axes titles
      fig1a.update_yaxes(title_text="Moving Averages (MA)", secondary_y=False)
      fig1a.update_yaxes(title_text="PRICE(USD)", secondary_y=True)

      # Show the plot
      st.plotly_chart(fig1a, use_container_width=True)


    with col_e:
      st.subheader('LONG TERM MOVING AVERAGE')

      # Create subplots
      fig1a = make_subplots(specs=[[{"secondary_y": True}]])

      # Add scatter plot for Volume
      fig1a.add_trace(
          go.Scatter(
              x=df3['TIMESPAN'],
              y=df3['PRICE_USD'],
              name="Price",
              mode="lines",
              marker_color='mintcream'
          ),
          secondary_y=True
      )

      # Add scatter plot for MOV_AVG_50DAYS
      fig1a.add_trace(
          go.Scatter(
              x=df3['TIMESPAN'],
              y=df3['MOV_AVG_50DAYS'],
              name="MA_50",
              mode="lines",
              marker_color='yellow'
          ),
          secondary_y=False
      )

      # Add scatter plot for MOV_AVG_200DAYS
      fig1a.add_trace(
          go.Scatter(
              x=df3['TIMESPAN'],
              y=df3['MOV_AVG_200DAYS'],
              name="MA_200",
              mode="lines",
              marker_color='red'
          ),
          secondary_y=False
      )


      # Update x-axis title
      fig1a.update_xaxes(title_text="Timespan")

      # Set y-axes titles
      fig1a.update_yaxes(title_text="Moving Averages (MA)", secondary_y=False)
      fig1a.update_yaxes(title_text="PRICE(USD)", secondary_y=True)

      # Show the plot
      st.plotly_chart(fig1a, use_container_width=True)

  col_f, col_g = st.columns(2)
  with col_f:
    st.markdown("""
    A rising moving average signals a bullish trend, while a falling moving average points to a bearish trend. In this case, we can see a heavy bullish trend.

If the 20-day moving average is above the 50-day moving average (as shown on the graph), it generally means that the short-term trend is more bullish than the long-term trend. This suggests that the price has been rising faster over the past 20 days than it has over the past 50 days, indicating upward momentum in the market. This effect can be observed from mid-October. Although both moving averages are rising at a fast pace.

A similar trend can be seen in the ETH and UNI tokens, occurring a few days after that of BTC.
    """)

  with col_g:
    st.markdown("""
    When the 200-day moving average falls below the 50-day moving average, it’s generally a sign of a short-term bullish trend for the asset’s price. This is because the 200-day average reflects a longer-term trend, while the 50-day average shows a shorter-term trend.

If the 50-day average is nearing the 200-day average but hasn’t crossed it yet, this could signal a potential change in trend. This is sometimes called a “golden cross” and is seen as a bullish signal by some traders. However, in this case, it’s actually a bullish signal. It is observed that the shorter-term trend has gained momentum and has crossed above the longer-term trend, leading to higher prices.   
    """)

  st.write("SOURCE:[Flipsidecrypto](https://flipsidecrypto.xyz/edit/queries/987bba9c-9885-498f-bb3e-026a0fe7abb8)")
  

  st.markdown(f'<h1 style="font-weight:bold;font-family:Georgia;font-size:30px;text-align:center;text-shadow: 5px 5px black;color:#f23a7d;">{"Top Tokens Based on Their 24-hours Trading Volume"}</h1>', unsafe_allow_html=True)


  url_a = 'https://api.alternative.me/v2/ticker/'
  df_a = pd.read_json(url_a)
  df = json_normalize(df_a['data'])#.transpose()
  # Convert column names to strings
  df.columns = df.columns.astype(str)
  # Drop the 'id' column
  df = df.drop('id', axis=1)
  df = df.drop('total_supply', axis=1)
  df = df.drop('website_slug', axis=1)
  # Replace the prefix for columns under 'quotes.USD'
  df.columns = df.columns.str.replace('quotes.USD.', '')

  # Remove the last three columns containing the repetition of 'percentage_change...'
  df = df.iloc[:, :-3]

  # Convert 'last_updated' to timestamp
  # df['last_updated'] = pd.to_datetime(df['last_updated'], unit='s')


  # Format the DataFrame to show arrows for increase and decrease
  formatted_df = df.copy()

  # Define a mapping function to replace values with arrows
  def format_arrows(value):
      if isinstance(value, (int, float)):
          if value > 0:
              return f'🔼 {value:.5g}'
          elif value < 0:
              return f'🔻 {abs(value):.5g}'
      return value

  # Apply the formatting function to relevant columns
  formatted_df['percentage_change_1h'] = formatted_df['percentage_change_1h'].apply(format_arrows)
  formatted_df['percentage_change_24h'] = formatted_df['percentage_change_24h'].apply(format_arrows)
  formatted_df['percentage_change_7d'] = formatted_df['percentage_change_7d'].apply(format_arrows)

  # Convert 'last_updated' to timestamp and calculate time difference
  formatted_df['last_updated'] = pd.to_datetime(formatted_df['last_updated'], unit='s')
  now = datetime.now()
  formatted_df['mins_ago'] = (now - formatted_df['last_updated']).dt.total_seconds() / 60  # Minutes ago

  # Display the formatted DataFrame using st.dataframe
  st.dataframe(formatted_df.drop('last_updated', axis=1))

  st.write("SOURCE:[Alternative.me](https://alternative.me/crypto/)")






# ____________________________________________________________________________________________________________________________________________________________________________



elif selected_menu_items == 'Greed & Fear Index':

  st.markdown(f'<h1 style="font-weight:bold;font-family:Georgia;font-size:60px;text-align:center;text-shadow: 5px 5px black;color:#f23a7d;">{"Greed & Fear Index"}</h1>', unsafe_allow_html=True)


  st.markdown("""
  The crypto fear and greed index is a tool that measures the dominant emotion of the cryptocurrency market, based on various indicators such as volatility, social media sentiment, market momentum, and surveys. The index ranges from 0 to 100, where 0 means extreme fear and 100 means extreme greed. The index can help investors to identify potential buying or selling opportunities, as well as to avoid emotional overreactions.

  The current value of the crypto fear and greed index is **68**, which indicates a state of **greed** in the market. This means that investors are feeling confident and optimistic about the future of cryptocurrencies, but it could also signal that the market is overbought and due for a correction. ⁵

  ### LOGIC
  To calculate the index which is a simple number from 0 to 100, where 0 means extreme fear and 100 means extreme greed. The index is based on five different factors, each weighted equally at 25%:

  - **Volatility**: This measures how much the price of bitcoin fluctuates compared to its average values in the last 30 and 90 days. A high volatility indicates a fearful market, while a low volatility indicates a greedy market.
  - **Market Momentum/Volume**: This measures how much trading activity and price movement there is in the market compared to its average values in the last 30 and 90 days. A high volume and momentum indicate a greedy market, while a low volume and momentum indicate a fearful market.
  - **Social Media**: This measures how much interest and engagement there is on social media platforms like Twitter and Reddit for bitcoin-related posts. A high interaction rate indicates a greedy market, while a low interaction rate indicates a fearful market.
  - **Surveys**: This measures the opinion of crypto investors through online polls conducted by strawpoll.com. A high percentage of bullish votes indicates a greedy market, while a high percentage of bearish votes indicates a fearful market.
  - **Dominance**: This measures the market share of bitcoin compared to other cryptocurrencies. A high dominance indicates a fearful market, as investors prefer to hold the most established and stable coin, while a low dominance indicates a greedy market, as investors seek higher returns from more risky and speculative coins.

  The index is calculated by averaging the scores of these five factors, each ranging from 0 to 100. The higher the index, the more greedy the market is, and vice versa. The index is updated daily and can be used as a tool to identify potential buying or selling opportunities, as well as to avoid emotional overreactions.
  """)

  st.markdown(f'<h1 style="font-weight:bold;font-family:Georgia;font-size:30px;text-align:center;text-shadow: 5px 5px black;color:#f23a7d;">{"Daily Updated Trend of Crypto Greed & Fear Index"}</h1>', unsafe_allow_html=True)
  
  col1, col2 = st.columns([1,2])
  with col1:

    button1 = """
  <script async src="https://static.coinstats.app/widgets/v3/cs-widget.js" ></script><cs-widget type="fear-and-greed"
theme="dark"
direction="horizontal"
background="#0D0D0D"
is-market-sentiment-visible="true"
is-last-updated-visible="true"
title-color="#FFFFFF"
chart-indicator-one-color="#F02935"
chart-indicator-two-color="#F07D29"
chart-indicator-three-color="#9ACB82"
chart-indicator-four-color="#34B349"
subtitle-color="#999999"
last-updated-color="#999999"
arrow-color="#262626"></cs-widget>
  """

    html(button1, height=400) #, width=220)

    st.write("SOURCE:[Coinstats.app](https://coinstats.app/new-widgets/fear-and-greed/)")

  url = 'https://api.alternative.me/fng/?limit=365&date_format=US'
  response = urlopen(url)
  data_json = json.loads(response.read())
  data = data_json['data'][:]

  df0 = pd.DataFrame(data)
  df0['timestamp'] = pd.to_datetime(df0['timestamp'])
  # df0.sort_values(by=['timestamp'])

  req = Request('https://flipsidecrypto.xyz/api/v1/queries/c0d1057d-2119-48c0-805f-43716b467d6a/data/latest', headers={'User-Agent': 'Mozilla/5.0'})
  response = urlopen(req).read()
  data = response.decode('utf-8')
  df1 = pd.read_json(data)
  
  

  # Get unique tokens for dropdown menu
  token_options = df1['TOKEN'].unique()

  # Streamlit app
  st.markdown(f'<h1 style="font-weight:bold;font-family:Georgia;font-size:30px;text-align:center;text-shadow: 5px 5px black;color:#f23a7d;">{"Token Price VS Fear & Greed Index(FGI) Chart"}</h1>', unsafe_allow_html=True)
  
  st.write("The chart below displays the prices of the top 30 tokens based on their 24-hour trading volume. To use this chart, the user can select the price of any token they want to compare to the FGI in the dropdown menu below. BTC is set as the default since insights drawn from the coin can be used as speculation for the crypto market as a whole. The color tiles indicate the labels for the FGI values, ranging from extreme greed to extreme fear.")

  sac.buttons([
      sac.ButtonsItem(label='LABEL', color='milk'),
      sac.ButtonsItem(label='Extreme Greed(>75)', color='gold'),
      sac.ButtonsItem(label='Greed(55-74)', color='limegreen'),
      sac.ButtonsItem(label='Neutral(45-54)', color='blue'),
      sac.ButtonsItem(label='Fear(25-44)', color='red'),
      sac.ButtonsItem(label='Extreme Fear(<25)', color='purple'),
      # sac.ButtonsItem(label='link', icon='share-fill', href='https://ant.design/components/button'),
  ], format_func='title', align='center', type='primary') #direction='vertical')

  # Dropdown for token selection
  selected_token = st.selectbox("Select Token", token_options)

  # Filter df1 based on selected token
  df1 = df1[df1['TOKEN'] == selected_token]

  fig = make_subplots(specs=[[{"secondary_y": True}]])

  # Add bar subplot with colors based on value_classification
  color_scale = {
    'Extreme Greed': 'gold',
    'Greed': 'limegreen',
    'Fear': 'red',
    'Neutral': 'blue',
    'Extreme Fear': 'purple'}
  colors = [color_scale[classification] for classification in df0['value_classification']]

  fig.add_trace(
      go.Scatter(
        x=df1['TIMESPAN'], 
        y=df1['PRICE_USD'], 
        name="Price", mode="lines",
        marker_color='mintcream',
        marker_size=10000),
      secondary_y=True
  )

  fig.add_trace(
      go.Bar(
        x=df0['timestamp'],
        y=df0['value'],
        name="FGI",
        marker_color=colors),
      secondary_y=False
  )

  fig.update_xaxes(title_text="Timespan")

  # Set y-axes titles
  fig.update_yaxes(title_text="Fear & Greed Index(FGI)", secondary_y=False)
  fig.update_yaxes(title_text="Price(USD)", secondary_y=True)

  st.plotly_chart(fig, use_container_width=True)

  st.write("SOURCE:[Alternative.me](https://alternative.me/crypto/), [Flipsidecrypto](https://flipsidecrypto.xyz/api/v1/queries/c0d1057d-2119-48c0-805f-43716b467d6a/data/latest)")

  st.markdown("""
  An obvious trend noticed in the above chart is that the prices of all tokens within the greed index are on a bullish run. Those in the neutral zone are often associated with the start or end of a bullish or bearish run, and finally, prices in the fear range are mostly bearish.

Also, the current greed index run is seen to be the longest in the past year, spanning close to three (3) months (since October). This can be an indicator that a bearish run is to be expected, but the SEC approval can even up the odds, and an even larger bullish run can be seen in recent days.
  """)


  # google_trend = """
  # <iframe width="100%" height="420" frameborder="0" src="https://www.theblock.co/data/alternative-crypto-metrics/web-traffic/google-search-volumes/embed" title="Google Search Volumes"></iframe>
  # """

  # html(google_trend, height=500) #, width=220)

  with col2:
    figa = px.line(df0, x="timestamp", y="value", title="Daily Crypto Fear & Greed Index", height=400)
    figa.update_layout(hovermode="x unified")
  # figa.add_scatter(x=df1['TIMESPAN'], y=df1['PRICE_USD'])
    st.plotly_chart(figa, use_container_width=True)

    st.write("SOURCE:[Alternative.me](https://alternative.me/crypto/)")



# ____________________________________________________________________________________________________________________________________________________________________________



# elif selected_menu_items == 'Useful Widgets':

#   col1, col2, col3 = st.columns(3)
#   with col1:

#     button1 = """
#   <script async src="https://static.coinstats.app/widgets/v3/cs-widget.js" ></script><cs-widget type="fear-and-greed"
# theme="dark"
# direction="horizontal"
# background="#0D0D0D"
# is-market-sentiment-visible="true"
# is-last-updated-visible="true"
# title-color="#FFFFFF"
# chart-indicator-one-color="#F02935"
# chart-indicator-two-color="#F07D29"
# chart-indicator-three-color="#9ACB82"
# chart-indicator-four-color="#34B349"
# subtitle-color="#999999"
# last-updated-color="#999999"
# arrow-color="#262626"></cs-widget>
#   """

#     html(button1, height=1000) #, width=220)

#   with col2:

#     button3 = """
#   <script async src="https://static.coinstats.app/widgets/v3/cs-widget.js" ></script><cs-widget type="crypto-profit-calculator"
# theme="dark"
# background="#0D0D0D"
# text-color="#FFFFFF"
# percentage-and-up="#6CCF59"
# percentage-and-down="#FF4D4D" coin='{"label":"BNB","coinId":"binance-coin","image":{"src":"https://static.coinstats.app/coins/1666608145347.png","alt":"BNB"},"coinName":"BNB","coinPrice":291.1715574041507}'></cs-widget>
#   """
#     html(button3, height=1000) #, width=220)

