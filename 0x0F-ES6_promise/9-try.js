export default function guardrail(mathFunction) {
  const queue = [];
  try {
    queue.push(mathFunction());
  } catch (e) {
    queue.push(e.message);
  }
  queue.push('Guardrail was processed');
  return queue;
}
