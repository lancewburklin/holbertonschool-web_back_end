import { uploadPhoto, createUser } from './utils';

function handleProfileSignup() {
  const first = uploadPhoto();
  const second = createUser();
  return Promise.all([first, second]).then((values) => {
    console.log(`${values[0].body} ${values[1].firstName} ${values[1].lastName}`);
  }).catch(() => console.log('Signup system offline'));
}
export default handleProfileSignup;
