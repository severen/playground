/// Calculate the powerset of a set.
fn powerset<T: Clone>(set: &[T]) -> Vec<Vec<T>> {
  let mut powerset = Vec::new();

  for mask in 0..1 << set.len() {
    let mut subset = Vec::new();

    for (i, x) in set.iter().enumerate() {
      if (mask & 1 << i) != 0 {
        subset.push(x.clone());
      }
    }

    powerset.push(subset);
  }

  powerset
}
