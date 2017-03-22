/**
 * Created by juwaini on 09/03/2017.
 */

angular.module('pacerApp', [])

    .config(['$httpProvider', function($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }])

    .controller('patientCtrl', ['$scope', '$http', function ($scope, $http) {

        angular.element(document).ready(function () {
            var url = 'api/patients';
            $http.get(url).then(function (res) {
                console.log(res.data);
            });
        });

        $scope.hint = {
            full_name: 'Key in patient name',
            date_of_birth: '01/01/1970',
            sex: 'Select Sex',
            parent_name: 'Key in parent name',
            language: 'Select Main Language',
            contact_number: 'e.g 010-1111222',
            email: 'e.g test@gmail.com',
            address: 'Please enter the address',
            postcode: 'e.g 50100',
            town: 'e.g Shah Alam',
            state: 'e.g Selangor',
            country: 'e.g Malaysia'
        };

        $scope.patientForm = {
            full_name: '',
            date_of_birth: '',
            sex: '',
            parent_name: '',
            language: '',
            contact_number: '',
            email: '',
            address: '',
            postcode: '',
            town: '',
            state: '',
            country: ''
        };

        $scope.patientFormSubmit = function(){
            $scope.patientForm.csrfmiddlewaretoken = $('#csrfmiddlewaretoken').val();
            console.log($scope.patientForm);

            var url = "api/patients/";

            $http.post(url, $scope.patientForm).then(function (res) {
                alert(res.data);
                $('#add-patient-modal').modal('toggle');
            });
        };
    }]);