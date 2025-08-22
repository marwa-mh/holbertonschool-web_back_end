export default function getListStudentIds(listofObjs) {
    if (!(listofObjs instanceof Array)) {
        return [];
    }
    return listofObjs.map((obj) => obj.id);
};
