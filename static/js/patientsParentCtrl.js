/**
 * Created by juwaini on 09/03/2017.
 */

angular
    .module('pacerApp')

    .config(['$httpProvider', function($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }])

    .controller('patientsParentCtrl', ['$scope', '$http', function ($scope, $http) {

        angular.element(document).ready(function () {
            $scope.patient_id = parseInt($('#patient_id').val());
            $scope.parentForm.patient_id = $scope.patient_id;
            loadTableData('load');
        });

        $scope.hint = {
            full_name: 'Key in parent name',
            id_number: 'i.e: IC No or Passport',
            //date_of_birth: '01/01/1970',
            //sex: 'Select Sex',
            //language: 'Select Main Language',
            contact_number: 'e.g 010-1111222',
            email: 'e.g test@gmail.com',
            address: 'Please enter the address',
            postcode: 'e.g 50100',
            town: 'e.g Shah Alam',
            state: 'e.g Selangor',
            country: 'e.g Malaysia'
        };

        $scope.parentForm = {
            patient_id: null,
            full_name: '',
            id_number: '',
            //date_of_birth: '',
            //sex: '',
            //language: '',
            contact_number: '',
            email: '',
            address: '',
            postcode: '',
            town: '',
            state: '',
            country: ''
        };

        $scope.parentFormSubmit = function(){
            var url = "/api/parents/";

            console.log($scope.parentForm);

            $http.post(url, $scope.parentForm).then(function (res) {
                 alert(res.data);
                 $('#add-parent-modal').modal('toggle');
                 loadTableData('reload');
             });
        };

        function loadTableData(action) {
            var url = '/api/parents/';
            var parentTable = $('#parent-table');
            var tableData = [];

            $http.get(url).then(function (res) {
                var json = res.data;
                var idx = 0;
                for (var i=0; i < json.length; i++)
                {
                    if (json[i].parent_of == $scope.patient_id)
                    {
                        idx++;
                        var tmpData = [];
                        tmpData.push(idx);
                        tmpData.push(json[i].full_name);
                        tmpData.push(json[i].id_number);
                        tmpData.push(json[i].contact_number);
                        tmpData.push('Action');
                        tableData.push(tmpData);
                    }

                }

                if (action == 'reload')
                {
                    parentTable.DataTable().destroy();
                }

                parentTable.DataTable({
                    data: tableData,
                    columns:
                        [
                            {'title': 'No'},
                            {'title': 'Parent/Guardian Name'},
                            {'title': 'ID No'},
                            {'title': 'Contact Number'},
                            {'title': 'Action'}
                        ]
                });

            });
        }

    }]);