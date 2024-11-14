# python-but-not-slow

This is an example repo showing how to write a high-level backend in Python that calls down to Rust when performance matters.

Not every team will want to invest in Rust fully, especially on teams with less technical expertise, but the case should be made for including it in code hot paths where Python struggles.

## Running the Application

To setup the local dev environment, run the following:

1. `maturin develop`
2. `pip install -e .`

Now to run the application:

`litestar --app pbns.main:app run`

In a new window, run the load tester:

`drill -b benchmark.yml -s`
