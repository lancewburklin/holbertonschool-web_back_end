import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const first = signUpUser(fileName, lastName);
  const second = uploadPhoto(fileName);
  return Promise.allSettled([first, second]).then((values) => values);
}
