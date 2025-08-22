export default function getStudentIdsSum(listOfStudents) {
    return listOfStudents.map((student) => student.id).reduce((accumulator, currentValue) => accumulator + currentValue);
};