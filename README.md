# FlashV2 Analysis

## ENV SETUP

```
virtualenv .flashV2-analysis
source .flashV2-analysis/bin/activate
git init
pip install jupyterlab jupyterthemes jupyterlab_darkside_ui cadCAD cadCAD_diagram matplotlib pandas plotly ipywidgets numpy networkx scipy seaborn python-dotenv psycopg2 psycopg2-binary statsmodels
jupyter labextension install jupyterlab-plotly
python -m ipykernel install --user --name=.flashV2-analysis
```

## RUN

```
jupyter-lab
jupyter notebook [OLD]
```

## POSTGRES

Start the postgresql service, create the flashv2 database, and enter the postgres environment:

```
brew services start postgresql
createdb flashv2
psql flashv2
```

Create the database admin and add privileges:

```
CREATE USER flashv2admin WITH PASSWORD [password];
GRANT ALL PRIVILEGES ON DATABASE flashv2 TO flashv2admin;

CREATE TABLE stakes (FromAddress text,
    StakeTransactionHash text,
    StakeID text PRIMARY KEY,
    StakeDateTime date,
    AmountIn decimal,
    MintedAmount decimal,
    ExpireDateTime date,
    TotalStakedDays decimal,
    DappRewardAmount decimal,
    DappPoolAddress text,
    UnstakeTransactionHash text,
    UnstakeDateTime date,
    UnstakeEarlyBurnedAmount decimal,
    MatchedAmount decimal,
    FlashVersion integer,
    V2MigrationTransactionHash text
);
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO flashv2admin;
```

```
CREATE TABLE uniswap (date date,
    liquidity decimal,
    value decimal,
    price decimal
);
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO flashv2admin;
```
