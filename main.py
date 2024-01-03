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
      sac.MenuItem('home', icon='house-fill'),
      sac.MenuItem('Fundamental Analysis', icon='box-fill'),
      sac.MenuItem('Technical Analysis', icon='git',),
      sac.MenuItem('Greed & Fear Index', icon='google'),
      sac.MenuItem('Useful Widgets', icon='Widgets')
      ])

  # ], format_func='title', open_all=True)

#     # Check if a menu item is selected
#     if selected_menu_items and len(selected_menu_items) > 0:
#         session_state.selected_menu_item = selected_menu_items[0]

# # Print the selected menu item
# if session_state.selected_menu_item:
#     st.header(f"Selected Menu Item: {session_state.selected_menu_item}")




# ____________________________________________________________________________________________________________________________________________________________________________


if selected_menu_items == 'home':
  sac.buttons([
      sac.ButtonsItem(label='button'),
      sac.ButtonsItem(icon='apple'),
      sac.ButtonsItem(label='google', icon='google', color='#25C3B0'),
      sac.ButtonsItem(label='wechat', icon='wechat'),
      sac.ButtonsItem(label='disabled', disabled=True),
      sac.ButtonsItem(label='link', icon='share-fill', href='https://ant.design/components/button'),
  ], format_func='title', align='center')

  #DIVIDER
  sac.divider(label='Divider', icon='house', align='center')
  st.subheader("Home")




# ____________________________________________________________________________________________________________________________________________________________________________
  

elif selected_menu_items == 'Fundamental Analysis':
  st.subheader("Crypto Market Cap")

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

  
  

  st.subheader("DEX Trading Volume Vs Moving Averages(20, 50 and 200 days)")

  # Sample data
  url = 'https://flipsidecrypto.xyz/api/v1/queries/dc27d475-6e02-4b73-9649-85155888fbf2/data/latest'
  req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
  response = urlopen(req).read()
  data = response.decode('utf-8')
  df2 = pd.read_json(data)

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


  st.subheader("DEX Trading Transactions(Swaps) Vs Moving Averages(20, 50 and 200 days)")

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






# ____________________________________________________________________________________________________________________________________________________________________________



elif selected_menu_items == 'Greed & Fear Index':
  st.subheader("Greed & Fear Index")

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
  st.title("Token Price and FGI Chart")

  sac.buttons([
      sac.ButtonsItem(label='LABEL', color='milk'),
      sac.ButtonsItem(label='Extreme Greed', color='gold'),
      sac.ButtonsItem(label='Greed', color='limegreen'),
      sac.ButtonsItem(label='Neutral', color='blue'),
      sac.ButtonsItem(label='Fear', color='red'),
      sac.ButtonsItem(label='Extreme Fear', color='purple'),
      sac.ButtonsItem(label='link', icon='share-fill', href='https://ant.design/components/button'),
  ], format_func='title', align='center', type='link') #direction='vertical')

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


  google_trend = """
  <iframe width="100%" height="420" frameborder="0" src="https://www.theblock.co/data/alternative-crypto-metrics/web-traffic/google-search-volumes/embed" title="Google Search Volumes"></iframe>
  """

  html(google_trend, height=500) #, width=220)

  with col2:
    figa = px.line(df0, x="timestamp", y="value", title="Daily Crypto Fear & Greed Index", height=400)
    figa.update_layout(hovermode="x unified")
  # figa.add_scatter(x=df1['TIMESPAN'], y=df1['PRICE_USD'])
    st.plotly_chart(figa, use_container_width=True)



# ____________________________________________________________________________________________________________________________________________________________________________



elif selected_menu_items == 'Useful Widgets':

  col1, col2, col3 = st.columns(3)
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

    html(button1, height=1000) #, width=220)

  with col2:

    button3 = """
  <script async src="https://static.coinstats.app/widgets/v3/cs-widget.js" ></script><cs-widget type="crypto-profit-calculator"
theme="dark"
background="#0D0D0D"
text-color="#FFFFFF"
percentage-and-up="#6CCF59"
percentage-and-down="#FF4D4D" coin='{"label":"BNB","coinId":"binance-coin","image":{"src":"https://static.coinstats.app/coins/1666608145347.png","alt":"BNB"},"coinName":"BNB","coinPrice":291.1715574041507}'></cs-widget>
  """
    html(button3, height=1000) #, width=220)

