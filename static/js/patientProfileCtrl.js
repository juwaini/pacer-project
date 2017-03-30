/**
 * Created by juwaini on 09/03/2017.
 */

angular
    .module('pacerApp')

    .config(['$httpProvider', function($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }])

    .controller('patientProfileCtrl', ['$scope', '$http', function ($scope, $http) {

        angular.element(document).ready(function () {
            $scope.patient_id = parseInt($('#patient_id').val());
            $scope.loadPatientProfile($scope.patient_id);
        });

        $scope.hint = {
            sex: 'Select Sex',
        };

        $scope.loadPatientProfile = function(patient_id){
            var url = "/api/patient/" + patient_id;

            $http.get(url).then(function (res) {
                var data = res.data;
                $scope.patientProfile = {
                    patient_id: data.patient_id,
                    full_name: data.full_name,
                    id_number: data.id_number,
                    date_of_birth: new Date(data.date_of_birth),
                    sex: data.sex,
                    address: data.address,
                    postcode: data.postcode,
                    town: data.town,
                    state: data.state,
                    country: data.country
                };
            });
        };

        // $scope.parentFormSubmit = function(){
        //     var url = "/api/parents/";
        //
        //     console.log($scope.parentForm);
        //
        //     $http.post(url, $scope.parentForm).then(function (res) {
        //          alert(res.data);
        //          $('#add-parent-modal').modal('toggle');
        //          loadTableData('reload');
        //      });
        // };

    }]);