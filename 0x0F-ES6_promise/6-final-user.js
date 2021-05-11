import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const first = signUpUser(firstName, lastName);
  const second = uploadPhoto(fileName);
  return Promise.allSettled([first, second]).then((values) => {
    const reArray = [];
    values.forEach((value) => {
      reArray.push({ status: value.status, value: value.value });
    });
    return reArray;
  });
}
