export default function createReportObject(employeesList) {
  return {
    allEmployess: { ...employeesList },
    getNumberOfDepartments(employeesList) {
      return Object.keys(employeesList).length;
    },
  };
}
