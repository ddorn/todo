export function attributes(key, todos) {
  let set = {};
  Object.values(todos).map(item => (set[item[key]] = true));
  return Object.keys(set).sort();
}

export function groupBy(what, todos) {
  let groups = {};
  Object.values(todos).forEach(item => {
    const value = item[what];
    if (value in groups) {
      groups[value].push(item);
    } else {
      groups[value] = [item];
    }
  });
  return groups;
}

export function filterObject(obj, f) {
  let n = {};
  Object.entries(obj).map((k) => {
    let [key, value] = k;
    if (f(value)) {
      n[key] = value
    }
  });
  return n;
}

export function cmpTodos(a, b) {
  let ddone = a.done - b.done,
    dimportant = b.important - a.important;
  return ddone || dimportant || a.categ.localeCompare(b.categ) || a.name.localeCompare(b.name);
}

export function range(length) {
  // JavaScript is a shame
    return new Array(length).fill(0).map((_, i) => i);
}


