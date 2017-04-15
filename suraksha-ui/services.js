angular.module('suraksha').service('QuizService', function ($rootScope, $http, $q, $state) {
    var user = {
        city: '',
        age: '',
        gender: ''
    };
    var userId;
    var subjects;
    var level;
    var currentSub;
    var currentLevelData;
    var currentQnNumber;
    var responseArray = [];
    var thisService = this;
    var score;
    var totalScore;
    var answerStatus;


    this.initialise = function () {
        score = 0;
        totalScore = 0;
        responseArray = [];
        level = 1;
        var deferred = $q.defer();
        $http({
            method: 'GET',
            url: $rootScope.baseURL + 'select_subject/'
        }).then(function successCallback(response) {
            subjects = response.data;
            deferred.resolve(subjects);
        }, function errorCallback(response) {
            console.log(response);
            deferred.reject();
        });
        return deferred.promise;
    };

    this.getSubjects = function () {
        return subjects;
    };

    this.getLevel = function () {
        return level;
    };

    this.setUserDetails = function (city,age,gender) {
        var deferred = $q.defer();
        user.city = city;
        user.age = age;
        user.gender = gender;

        $http({
            method: 'POST',
            url: $rootScope.baseURL + 'users/',
            headers: {
                'Content-Type': 'application/json'
            },
            data: user
        }).then(function successCallback(response) {
            userId = response.data.id;
            deferred.resolve();
        },function errorCallback(response) {
            deferred.reject();
        });
        return deferred.promise;


    };

    this.beginLevel = function (selectedSubject) {
        currentQnNumber = 0;
        var deferred = $q.defer();
        currentSub = selectedSubject;
        console.log(user.city,level,currentSub);
        $http({
            method: 'GET',
            url: $rootScope.baseURL + 'questions/',
            params: {
                city: user.city,
                level: level,
                subject: currentSub
            }
        }).then(function successCallback(response) {
            console.log(response);
            currentLevelData = response.data;
            if(response.data.questions.length > 0){
                deferred.resolve(response.data);
            }else{
                deferred.reject();
            }
        }, function errorCallback() {
            alert('Server Error');
            $state.go('home');
        });
        return deferred.promise;
    };

    this.getCurrentLevelData = function () {
        return currentLevelData;
    };

    this.getCurrentQuestion = function () {
        return currentLevelData['questions'][currentQnNumber];
    };

    this.nextQuestion = function () {
        $rootScope.loading = true;
        currentQnNumber++;
        if (currentQnNumber > currentLevelData.questions.length - 1) {
            level++;
            thisService.beginLevel(currentSub).then(function () {
                $http({
                    method: 'POST',
                    url: $rootScope.baseURL + 'questions/',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    data: {
                        user: userId,
                        response: responseArray
                    }
                }).then(function successCallback(response) {
                    responseArray = [];
                    $rootScope.$broadcast('LEVELCHANGE');
                    $rootScope.loading = false;
                },function errorCallback(response) {
                    $rootScope.loading = false;
                    alert('Server Error');
                    responseArray = [];
                    $state.go('home');
                });
            },function () {
                $http({
                    method: 'POST',
                    url: $rootScope.baseURL + 'questions/',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    data: {
                        user: userId,
                        response: responseArray
                    }
                }).then(function successCallback(response) {
                    responseArray = [];
                    $rootScope.$broadcast('QUIZFINISHED');
                    $rootScope.loading = false;
                },function errorCallback(response) {
                    $rootScope.loading = false;
                    alert('Server Error');
                    responseArray = [];
                    $state.go('home');
                });
            });
        } else {
            $rootScope.loading = false;
            $rootScope.$broadcast('QUESTION:ready');
        }
        // $rootScope.$apply();
    };

    $rootScope.$on('USERRESPONSE', function ($event, data) {
        if(data.optionId == 0){
            score++;
            totalScore++;
            answerStatus = 'correct'
        }
        else{
            totalScore++;
            answerStatus = 'incorrect'
        }
        responseArray.push(data);
        console.log(responseArray);
    });

    this.getScore = function () {
        return score;
    };

    this.getTotalScore = function () {
        return totalScore;
    };

    this.getAnswerStatus = function () {
        return answerStatus;
    };
});