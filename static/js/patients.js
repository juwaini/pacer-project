/**
 * Created by juwaini on 09/03/2017.
 */

var patient_form = new Vue({
    el: '#patient-form',
    data: {
        formData: {
            //csrfmiddlewaretoken: this.$el.csrfmiddlewaretoken.value,
            sex: '',
            language: ''
        },
    },
    methods: {
        on_add_patient_submit: function (event) {
            console.log(this.$el.csrfmiddlewaretoken.value);
        }
    }
});