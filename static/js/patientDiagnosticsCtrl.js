/**
 * Created by juwaini on 09/03/2017.
 */

angular
    .module('pacerApp')

    .config(['$httpProvider', function($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }])

    .controller('patientDiagnosticsCtrl', ['$scope', '$http', function ($scope, $http) {

        angular.element(document).ready(function () {
            $scope.patient_id = parseInt($('#patient_id').val());
            $scope.loadDiagnostics($scope.patient_id);
        });

        $scope.hint = {
            diagnostic: 'Please key in the diagnostic',
        };

        $scope.diagnosticsForm = {
            diagnostic: '',
            patient_id: '',
        };

        $scope.diagnostics = [];

        $scope.loadDiagnostics = function(patient_id){
            var url = "/api/diagnostics";

            $http.get(url).then(function (res) {
                var data = res.data;
                //console.log(res.data);
                var data_size = data.length;
                for(var i=0; i < data_size; i++)
                {
                     if(data[i].diagnostic_for == patient_id)
                         $scope.diagnostics.push(data[i]);
                }
                console.log($scope.diagnostics);
            });
        };

        $scope.diagnosticsFormSubmit = function(){
            var url = "/api/diagnostics";
            $scope.diagnosticsForm.patient_id = $scope.patient_id;
            console.log($scope.diagnosticsForm);
            $http.post(url, $scope.diagnosticsForm).then(function (res) {
                 alert(res.data);
                 $scope.diagnostics = [];
                 $scope.loadDiagnostics($scope.patient_id);
                 $scope.diagnosticsForm.diagnostic = '';
             });
        };

    }]);