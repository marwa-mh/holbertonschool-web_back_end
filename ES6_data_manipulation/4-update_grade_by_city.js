export default function updateStudentGradeByCity(listOfStudents, city, newGrades) {
    return listOfStudents.filter((student) => student.location === city)
           .map((student) => {
            const gradeObj = newGrades.find((grade) => grade.studentId === student.id);
            return {
                ...student,
                grade: gradeObj ? gradeObj.grade : 'N/A',
            };
           });
}