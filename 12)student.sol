pragma solidity ^0.8.0;

contract StudentDB{

    struct Student{
        string name;
        uint256 rollno;
        string class;
    }

    Student[] private students;

    function addStudent(string memory name, uint256 rollno, string memory class) public {
        students.push (Student(name, rollno, class));
    }

    function getStudentById(uint256 id) public view returns (string memory, uint256, string memory class) {
        require(id < students.length, "Student does not exist in database");
        return(students[id].name, students[id].rollno, students[id].class);
    }

    function getTotalNumberOfStudents() public view returns (uint256){
        return students.length;
    }

}







/*

// SPDX-License-Identifier: MIT
pragma solidity >=0.7.0;

contract StudentManagement {

    struct Student {
        int stud_id;
        string name;
        string department;
    }

    Student[] public students;

    // Function to add a student to the list
    function addStudent(int stud_id, string memory name, string memory department) public {
        Student memory student = Student(stud_id, name, department);
        students.push(student);
    }

    // Function to retrieve a student by their ID
    function getStudent(int stud_id) public view returns (string memory, string memory) {
        for (uint i = 0; i < students.length; i++) {
            if (students[i].stud_id == stud_id) {
                return (students[i].name, students[i].department);
            }
        }
        return ("Name Not Found", "Department Not Found");
    }

    // Fallback function triggered when the contract receives Ether without data
    fallback() external payable {
        students.push(Student(7, "XYZ", "Computer Science"));
    }

    // Receive function triggered when Ether is sent to the contract with no calldata
    receive() external payable {
        // No specific action is defined here
    }
}


*/