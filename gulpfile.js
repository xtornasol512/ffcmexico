var gulp = require('gulp');

var concat = require('gulp-concat');
var uglify = require('gulp-uglify');

var minifyHtml = require('gulp-minify-html'); 

gulp.task('scripts', function(){
    gulp.src('./temp/source/js/*.js')
        .pipe(uglify())
        .pipe(concat('all.js'))
        .pipe(gulp.dest('./temp/dist/'))
});

gulp.task('default', function(){

});
