import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="The Fair Game",
    layout="wide"
)

# ---------------------------------------------------
# LOAD CSV FILES
# ---------------------------------------------------

free_market_df = pd.read_csv(
    "free_market.csv"
)

welfare_df = pd.read_csv(
    "welfare_society.csv"
)

egalitarian_df = pd.read_csv(
    "egalitarian_utopia.csv"
)

comparison_df = pd.read_csv(
    "comparison.csv"
)

lorenz_df = pd.read_csv(
    "lorenz.csv"
)

# ---------------------------------------------------
# CSS
# ---------------------------------------------------

st.markdown(
    """
    <style>

div[role="radiogroup"] {
    display: flex;
    justify-content: center;
    gap: 18px;
    margin-top: 10px;
    margin-bottom: 40px;
    flex-wrap: wrap;
}

div[role="radiogroup"] label {
    background: #111827;
    border: 1px solid #374151;
    border-radius: 14px;
    padding: 14px 22px;
    min-width: 210px;
    text-align: center;
    transition: all 0.25s ease;
}

div[role="radiogroup"] label:hover {
    transform: translateY(-2px);
    border: 1px solid #67e8f9;
    background: #1f2937;
}

div[role="radiogroup"] p {
    color: white !important;
    font-size: 18px !important;
    font-weight: 700 !important;
}

div[role="radiogroup"] label[data-baseweb="radio"] > div:first-child {
    display: none;
}

    .stApp {
        background-color: #050816;
        color: white;
    }

    h1 {
    color:#67e8f9 !important;
    font-weight:800;
    font-size:72px !important;
    letter-spacing :2px;
}

    h2, h3 {
        color: #ff4df0 !important;
    }

    .metric-card {
        background: rgba(20,20,40,0.85);
        padding: 20px;
        border-radius: 20px;
        border: 1px solid #00f7ff;
        text-align: center;
        box-shadow: 0px 0px 15px rgba(0,247,255,0.4);
        margin-bottom: 20px;
        transition: 0.3s ease;
    }

    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0px 0px 25px rgba(0,247,255,0.8);
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------
# NAVBAR
# ---------------------------------------------------

page = st.radio(
    "",
    [
        "Project Overview",
        "The Free Market",
        "The Welfare Society",
        "The Egalitarian Utopia",
        "Comparative Analysis"
    ],
    horizontal=True
)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

if page == "Project Overview":
 st.title("⚖️ THE FAIR GAME")

 st.markdown(
    """
    A computational wealth distribution simulation
    exploring inequality, poverty, and redistribution
    under different economic systems.
    """
)


# ---------------------------------------------------
# CHART FUNCTION
# ---------------------------------------------------

def cyberpunk_chart(
    x,
    y1,
    y2,
    y3,
    title,
    ylabel
):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=x,
            y=y1,
            mode='lines+markers',
            name='Free Market'
        )
    )

    fig.add_trace(
        go.Scatter(
            x=x,
            y=y2,
            mode='lines+markers',
            name='Welfare Society'
        )
    )

    fig.add_trace(
        go.Scatter(
            x=x,
            y=y3,
            mode='lines+markers',
            name='Egalitarian Utopia'
        )
    )

    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='#050816',
        plot_bgcolor='#050816',
        height=600,
        title=title,
        xaxis_title='Rounds',
        yaxis_title=ylabel,
        hovermode='x unified'
    )

    return fig

# ---------------------------------------------------
# PROJECT OVERVIEW
# ---------------------------------------------------

if page == "Project Overview":

    st.markdown(
    """
    <h2 style='
        color:#ff4df0;
        font-size:34px;
        border-bottom:2px solid #ffcc00;
        padding-bottom:8px;
        margin-top:25px;
    '>
    PROJECT OVERVIEW
    </h2>
    """,
    unsafe_allow_html=True
)

    st.markdown(
        """
        The Fair Game is an agent-based economic
        simulation designed to study how wealth
        concentration and inequality emerge through
        repeated stochastic interactions.
        It also aims to observe how taxation and redistribution affect the dynamics using various economic metrics like the "Gini Coefficient" and the "Lorenz Curve".
        """
    ) 

    st.markdown(
    """
    <h2 style='
        color:#ff4df0;
        font-size:34px;
        border-bottom:2px solid #ffcc00;
        padding-bottom:8px;
        margin-top:25px;
    '>
    BASIC RULES
    </h2>
    """,
    unsafe_allow_html=True
)
    
    st.markdown(
        """
        - Each society begins with 1,000 agents, each initially possessing ₹1,000.
        - During every transaction, two agents are selected randomly.
        - Both agents contribute to a transaction stake equal to 5% of the wealth of the poorer agent.
        - One of the two agents is selected randomly as the winner, with both agents having an equal probability of winning the transaction.
        - 1 round of exchange consists of 100 transactions.
        - Each society is simulated for 100,000 rounds, corresponding to a total of 10 million transactions per society.
        - Any agent with wealth below ₹200 is classified as being in poverty.
        - Total wealth within the system is conserved throughout the simulation.
   """
    )
    st.markdown(
    """
    <h2 style='
        color:#ff4df0;
        font-size:34px;
        border-bottom:2px solid #ffcc00;
        padding-bottom:8px;
        margin-top:25px;
    '>
    The Simulation compares :
    </h2>
    """,
    unsafe_allow_html=True
)
    st.markdown(
    """
        - The Free Market (A "No Redistribution , No Taxation" society )
        - The Welfare Society (A "Moderate Redistribution , Moderate Taxation" society )
        - The Egalitarian Utopia (A "High Redistribution , High Taxation" society )
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class='metric-card'>
            <h2>1000</h2>
            <p>Agents</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class='metric-card'>
            <h2>100,000</h2>
            <p>Rounds</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
            <div class='metric-card'>
            <h2>₹1,000,000</h2>
            <p>Total Wealth</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# ---------------------------------------------------
# FREE MARKET
# ---------------------------------------------------

elif page == "The Free Market":

    st.markdown(
    """
    <div style='
        color:#ff4d6d;
        font-size:55px;
        font-weight:900;
        margin-top:30px;
        border-bottom:3px solid #9ca3af;
        padding-bottom:10px;
    '>
    THE FREE MARKET
    </div>
    """,
    unsafe_allow_html=True
    )

    st.markdown(
    """
    <h2 style='
        color:#ff4df0;
        font-size:34px;
        border-bottom:2px solid #ffcc00;
        padding-bottom:8px;
        margin-top:25px;
    '>
    REDISTRIBUTION AND TAXATION RULES
    </h2>
    """,
    unsafe_allow_html=True
)
    st.markdown(
        """

        - Nobody is taxed.
        - No welfare support for anyone.
        - No redistribution of wealth.
        - Wealth evolves entirely through transactions.
        """
    )

    st.dataframe(
        free_market_df,
        use_container_width=True
    )

    st.markdown(
    """
    <h2 style='
        color:#ff4df0;
        font-size:34px;
        border-bottom:2px solid #ffcc00;
        padding-bottom:8px;
        margin-top:25px;
    '>
    KEY INSIGHTS
    </h2>
    """,
    unsafe_allow_html=True
)
    st.markdown(
        """

        - Wealth concentration accelerates significantly over time, leading to extreme inequality within the system.
        - Median wealth collapses over time, with the typical agent retaining only around 2% of their initial wealth after 100,000 rounds.
        - A small minority accumulates disproportionate wealth with the top 100 agents holding ₹950,000/1,000,000 and the rest 900 holding just ₹50,000/1,000,000 .
        - Equal starting conditions alone are insufficient to prevent long-term inequality, as more than 85% of agents fall below ₹200 after 100,000 rounds
        """
    )

# ---------------------------------------------------
# WELFARE SOCIETY
# ---------------------------------------------------

elif page == "The Welfare Society":

    st.markdown(
    """
    <div style='
        color:#ff4d6d;
        font-size:55px;
        font-weight:900;
        margin-top:30px;
        border-bottom:3px solid #9ca3af;
        padding-bottom:10px;
    '>
    THE WELFARE SOCIETY
    </div>
    """,
    unsafe_allow_html=True
    ) 


    st.markdown(
    """
    <h2 style='
        color:#ff4df0;
        font-size:34px;
        border-bottom:2px solid #ffcc00;
        padding-bottom:8px;
        margin-top:25px;
    '>
    REDISTRIBUTION AND TAXATION RULES
    </h2>
    """,
    unsafe_allow_html=True
)

    st.markdown(
        """
        - Taxes and welfare support are introduced. 
        - Wealth above ₹1500 is taxed
        - 15% tax on surplus wealth charged every 1000 rounds.
        - The collected taxes are redistributed every 1000 rounds among agents with wealth less than ₹500.
        """
    )    

    st.dataframe(
        welfare_df,
        use_container_width=True
    )

    st.markdown(
    """
    <h2 style='
        color:#ff4df0;
        font-size:34px;
        border-bottom:2px solid #ffcc00;
        padding-bottom:8px;
        margin-top:25px;
    '>
    KEY INSIGHTS
    </h2>
    """,
    unsafe_allow_html=True
)
    st.markdown(
        """

        - Redistribution slows wealth concentration while still preserving upward mobility and wealth accumulation.
        - Median wealth remains more stable with the typical agent retaining more than 60% of their initial wealth after 100,000 rounds.
        - Market dynamics remain active while inequality is partially controlled with top 100 agents holding ₹330,000/1,000,000 and rest 900 holding ₹670,000/1,000,000 .
        - Poverty growth is moderated with just 67/1000 people having less than ₹200 after 100,000 rounds.

        """
    )

# ---------------------------------------------------
# EGALITARIAN UTOPIA
# ---------------------------------------------------

elif page == "The Egalitarian Utopia":

 st.markdown(
    """
    <div style='
        color:#ff4d6d;
        font-size:55px;
        font-weight:900;
        margin-top:30px;
        border-bottom:3px solid #9ca3af;
        padding-bottom:10px;
    '>
    THE EGALITARIAN UTOPIA
    </div>
    """,
    unsafe_allow_html=True
    ) 

 st.markdown(
    """
    <h2 style='
        color:#ff4df0;
        font-size:34px;
        border-bottom:2px solid #ffcc00;
        padding-bottom:8px;
        margin-top:25px;
    '>
    REDISTRIBUTION AND TAXATION RULES
    </h2>
    """,
    unsafe_allow_html=True
)
 st.markdown(
        """

        - Much aggressive taxes and greater welfare support.
        - Wealth above ₹1200 is taxed.
        - 45% tax on surplus wealth charged every 500 rounds.
        - The collected taxes are redistributed every 500 rounds among agents with wealth less than ₹700.
        """
    )

 st.dataframe(
        egalitarian_df,
        use_container_width=True
    )

 st.markdown(
    """
    <h2 style='
        color:#ff4df0;
        font-size:34px;
        border-bottom:2px solid #ffcc00;
        padding-bottom:8px;
        margin-top:25px;
    '>
    KEY INSIGHTS
    </h2>
    """,
    unsafe_allow_html=True
 )

 st.markdown(
        """

        - Wealth equality remains significantly higher while extreme wealth accumulation is strongly constrained.
        - Median wealth remains highly stable, with the typical agent retaining more than 90% of their initial wealth even after 100,000 rounds.
        - Upper-tail wealth concentration is constrained with top 100 agents having just ₹170,000/1,000,000 and rest 900 having ₹830,000/1,000,000.
        - Poverty is effectively eliminated, with no agent falling below ₹200 at the measured stages of the simulation.
        """
)
 

# ---------------------------------------------------
# COMPARATIVE ANALYSIS
# ---------------------------------------------------

elif page == "Comparative Analysis":

    st.markdown(
    """
    <div style='
        color:#ff4d6d;
        font-size:55px;
        font-weight:900;
        margin-top:30px;
        border-bottom:3px solid #9ca3af;
        padding-bottom:10px;
    '>
    COMPARITIVE ANALYSIS
    </div>
    """,
    unsafe_allow_html=True
    ) 

    fig1 = cyberpunk_chart(
        comparison_df['Rounds'],
        comparison_df['Free Median'],
        comparison_df['Welfare Median'],
        comparison_df['Egalitarian Median'],
        'Median Wealth vs Rounds',
        'Median Wealth'
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    fig2 = cyberpunk_chart(
        comparison_df['Rounds'],
        comparison_df['Free Top10'],
        comparison_df['Welfare Top10'],
        comparison_df['Egalitarian Top10'],
        'Top 10% Wealth Share vs Rounds',
        'Top 10% Wealth Share'
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    fig3 = cyberpunk_chart(
        comparison_df['Rounds'],
        comparison_df['Free Gini'],
        comparison_df['Welfare Gini'],
        comparison_df['Egalitarian Gini'],
        'Gini Coefficient vs Rounds',
        'Gini Coefficient'
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    fig4 = cyberpunk_chart(
        comparison_df['Rounds'],
        comparison_df['Free Poverty'],
        comparison_df['Welfare Poverty'],
        comparison_df['Egalitarian Poverty'],
        'Poverty Percentage vs Rounds',
        'Poverty Percentage'
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

    lorenz = go.Figure()

    lorenz.add_trace(
        go.Scatter(
            x=lorenz_df['Population Share'],
            y=lorenz_df['Free Market'],
            mode='lines',
            name='Free Market'
        )
    )

    lorenz.add_trace(
        go.Scatter(
            x=lorenz_df['Population Share'],
            y=lorenz_df['Welfare Society'],
            mode='lines',
            name='Welfare Society'
        )
    )

    lorenz.add_trace(
        go.Scatter(
            x=lorenz_df['Population Share'],
            y=lorenz_df['Egalitarian Utopia'],
            mode='lines',
            name='Egalitarian Utopia'
        )
    )

    lorenz.add_trace(
        go.Scatter(
            x=[0, 1],
            y=[0, 1],
            mode='lines',
            name='Perfect Equality',
            line=dict(dash='dash')
        )
    )

    lorenz.update_layout(
        template='plotly_dark',
        paper_bgcolor='#050816',
        plot_bgcolor='#050816',
        height=750,
        title='Lorenz Curve Comparison'
    )

    st.plotly_chart(
        lorenz,
        use_container_width=True
    )

    st.subheader("Final Comparison Table")

    st.dataframe(
        comparison_df,
        use_container_width=True
    )


    st.markdown(
    """
    <h2 style='
        color:#ff4df0;
        font-size:34px;
        border-bottom:2px solid #ffcc00;
        padding-bottom:8px;
        margin-top:25px;
    '>
    FINAL CONCLUSIONS
    </h2>
    """,
    unsafe_allow_html=True
 )

    st.markdown(
        """

     - Wealth inequality emerges even under initially equal conditions, despite every agent having an equal probability of gaining wealth in individual transactions.
     - The Free Market and Welfare Society maintain similar median wealth levels until around 5,000 rounds. Beyond that point, median wealth declines sharply in the Free Market, while remaining relatively stable in the Welfare Society. The Egalitarian Utopia maintains the highest long-term median wealth due to continuous redistribution.
     - Wealth concentration increases rapidly in the Free Market model, with the top 10% eventually controlling nearly all wealth. In contrast, redistribution mechanisms in the Welfare Society and Egalitarian Utopia significantly constrain upper-tail wealth accumulation.
     - After 100,000 rounds the Gini Coefficient for:
         - The Free Market records a Gini Coefficient of approximately 0.93, indicating extreme wealth concentration rarely seen in stable real world economies.
         - The Welfare Society stabilizes around 0.46, representing moderate inequality levels broadly comparable to mixed-market economies such as India and the USA, where redistribution exists but inequality remains significant.
         - The Egalitarian Utopia remains near 0.20, indicating highly equal wealth distribution similar to the lower inequality levels observed in Nordic-style welfare economies, though real societies rarely achieve such uniformity.
     - The Egalitarian Utopia never had any poverty at any stage of the simulation.
         - The Welfare Society plateaued at 6.5% poverty after 5000 rounds. 
         - However for the Free Market , the poverty percentage kept on increasing continuously with each round.
     - The Lorenz Curve gives the graphical represenation of wealth ineqality. 
         - The Egalitarian Utopia's curve is the closest to ideal representing great equality. 
         - It is followed by the Welfare Society which has the curve resembling a lot of real world economies like Sweden , Denmark. 
         - The curve for the Free Market is highly skewed and represents great wealth inequality.
     - The key lessons are :
         - Equality vs Opportunity is a trade off and the key is balance. 
         - Redistribution systems reduce inequality and poverty growth, though stronger redistribution also constrains upper-tail wealth accumulation.
         - The key is to not fall on either extreme while providing the citizens with incentives of working hard or making money and also providing them security.
        """
    )