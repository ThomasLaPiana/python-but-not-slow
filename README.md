# python-but-not-slow

This is an example repo showing how to write a high-level backend in Python that calls down to Rust when performance matters.

Not every team will want to invest in Rust fully, especially on teams with less technical expertise, but the case should be made for including it in code hot paths where Python struggles.

## Prerequisites

Before running this example, you'll need the following software:

* [maturin](https://github.com/PyO3/maturin)
* [drill](https://github.com/fcsonline/drill)
* Python 3.12.7

## Running the Application

To setup the local dev environment, run the following:

1. `maturin develop`
2. `pip install -e .`

Now to run the application:

`litestar --app pbns.main:app run`

In a new window, run the load tests:

`drill -b drill.yml -s`

Despite being an ultra-simplistic toy example, the results still show that even with the overhead of calling into Rust there is a significant performance increase and stabilization of tail latencies.
