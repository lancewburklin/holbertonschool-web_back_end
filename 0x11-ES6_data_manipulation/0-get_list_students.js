export default function getListStudents() {
  const items = [];
  items.push({ id: 1, firstName: 'Guillaume', location: 'San Francisco' });
  items.push({ id: 2, firstName: 'James', location: 'Columbia' });
  items.push({ id: 5, firstName: 'Serena', location: 'San Francisco' });
  return (items);
}
