/**
 * Created by juwaini on 09/03/2017.
 */

function onModalShown() {
    return new Vue({
        el: '#patient-form',
        data: {
            formData: {
                sex: '',
                language: '',
            },
        },
        methods: {
            on_add_patient_submit: function (event) {
                this.formData.csrfmiddlewaretoken = $('#csrfmiddlewaretoken').val();
                console.log(this.formData);
                this.$http.post('/api/patients/', this.formData);
                    //.then(alert('Successfully added!'), alert('Failed to add!'));
            },

            onModalDisplay: function (event) {
            },
        },
    });
};

$('#add-patient-modal').on('shown.bs.modal', function() {
    onModalShown();
});