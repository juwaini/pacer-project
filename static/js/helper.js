/**
 * Created by juwaini on 28/03/2017.
 */

function createClieckableLink(string_data, patient_id) {
    var base_url = 'patients/';
    var url = base_url + String(patient_id);
    return '<a href="' + url + '" target="_blank">' + string_data + '</a>';
}

function closeTab() {
    close();
}

function calculateAge(birthMonth, birthDay, birthYear)
{
  todayDate = new Date();
  todayYear = todayDate.getFullYear();
  todayMonth = todayDate.getMonth();
  todayDay = todayDate.getDate();
  age = todayYear - birthYear;

  if (todayMonth < birthMonth - 1)
  {
    age--;
  }

  if (birthMonth - 1 == todayMonth && todayDay < birthDay)
  {
    age--;
  }
  return age;
}