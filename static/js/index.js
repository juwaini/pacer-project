/**
 * Created by juwaini on 09/03/2017.
 */

angular.module('pacerApp', [])

    .config(['$httpProvider', function($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }])

    .controller('indexCtrl', ['$scope', '$http', function ($scope, $http) {

        angular.element(document).ready(function () {
            loadTableData('load');
        });

        $scope.hint = {
            full_name: 'Key in patient name',
            id_number: 'i.e: MyKid',
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
            id_number: '',
            date_of_birth: '',
            sex: '',
            parent_name: '',
            language: '',
            contact_number: [],
            email: '',
            address: '',
            postcode: '',
            town: '',
            state: '',
            country: ''
        };

        $scope.patientFormSubmit = function(){
            var url = "/api/patients/";

            $http.post(url, $scope.patientForm).then(function (res) {
                alert(res.data);
                $('#add-patient-modal').modal('toggle');
                loadTableData('reload');
            });
        };

        $scope.onDOBLostFocus = function() {
            var dob = $scope.patientForm.date_of_birth;
            var patient_age = calculateAge(dob.getMonth(), dob.getDate(), dob.getFullYear());
            if (patient_age < 18)
                $scope.parent1 = true;
            else
                $scope.parent1 = false;
        };

        $scope.checkChars = function() {
            if ($scope.patientForm.postcode.length === 5)
            {
                console.log("Valid postcode! " + $scope.patientForm.postcode);
            }
            else
            {
                console.log('Huh!?');
            }
        };

        $scope.onAddContactClick = function() {
            $scope.parent_ctx_div = true;
        };

        $scope.onCancelContactClick = function() {
            $scope.parent_ctx_div = false;
        };

        $scope.onAddEmailClick = function() {
            $scope.parent_email_div = true;
        };

        $scope.onCancelEmailClick = function() {
            $scope.parent_email_div = false;
        };

        $scope.onAddParentClick = function() {
            $scope.parent2 = true;
        };

        $scope.onCancelParentClick = function() {
            $scope.parent2 = false;
        };

        function loadTableData(action) {
            var url = '/api/patients';
            var patientTable = $('#patient-table');
            var tableData = [];

            $http.get(url).then(function (res) {
                var json = res.data;
                for (var i=0; i < json.length; i++)
                {
                    var tmpData = [];
                    tmpData.push(i+1);
                    tmpData.push(createClieckableLink(json[i].full_name, json[i].id));
                    tmpData.push(json[i].id_number);
                    tmpData.push(json[i].date_of_birth);
                    tmpData.push('Action');
                    tableData.push(tmpData);
                }

                if (action === 'reload')
                {
                    patientTable.DataTable().destroy();
                }

                patientTable.DataTable({
                    data: tableData,
                    columns:
                        [
                            {'title': 'No'},
                            {'title': 'Patient Name'},
                            {'title': 'ID No'},
                            {'title': 'Date of Birth'},
                            {'title': 'Action'}
                        ]
                });

            });
        }

    }]);