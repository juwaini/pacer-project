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