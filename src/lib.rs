use pyo3::prelude::*;

#[pyfunction]
pub fn fibonacci(n: i128) -> PyResult<i128> {
    if n < 0 {
        panic!("{} is negative!", n);
    } else if n == 0 {
        panic!("zero is not a right argument to fibonacci()!");
    } else if n == 1 {
        return Ok(1);
    }

    let mut sum = 0;
    let mut last = 0;
    let mut curr = 1;
    for _i in 2..n {
        sum = last + curr;
        last = curr;
        curr = sum;
    }
    Ok(sum)
}

#[pymodule]
fn _pbns(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fibonacci, m)?)?;
    Ok(())
}
