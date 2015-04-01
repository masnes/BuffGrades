TABLES = {
    'users_students': (
    "CREATE TABLE `users_students` ("
	"studentId int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,"
	"userNameId varchar(16) NOT NULL,"
	"courseId varchar(8) NOT NULL);"
    "  PRIMARY KEY (`studentID`)"
    ") ENGINE=InnoDB"),
	
	'personal_info': (
    "CREATE TABLE `personal_info` ("
	"personalInfoId int(11) AUTO_INCREMENT NOT NULL,"
	"userName varchar(16) NOT NULL,"
	"firstName varchar(16) NOT NULL,"
	"lastName varchar(16) NOT NULL,"
	"  PRIMARY KEY (`personalInfoId`)"
    ") ENGINE=InnoDB"),

	'courses': (
    "CREATE TABLE `courses` ("
	"id int(11) AUTO_INCREMENT NOT NULL,"
	"assignmentId int(8) NOT NULL,"
	"courseId varchar(8) NOT NULL,"
	"courseName varchar(30) NOT NULL,"
	"assignmentTypeId varchar(12) NOT NULL,"
	"  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"),

	'assignmentTypeId': (
	"CREATE TABLE assignmentTypeId ("
	"id int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,"
	"assignmentTypeID varchar(8) NOT NULL,"
	"assignmentId varchar(30) NOT NULL,"
	"typeName varchar(12) NOT NULL,"
	"typeWeight int(3) NOT NULL,"
	"numOfAssigns int(3) NOT NULL);"
	"PRIMARY KEY ('id')"
	") ENGINE=InnoDB"),
	
	'assignment': (
    "CREATE TABLE `assignment` ("
	"id int(11) AUTO_INCREMENT NOT NULL,"
	"assignmentID int(8) NOT NULL,"
	"assigmentTypeID varchar(16) NOT NULL,"
	"pointsPossible int(4) NOT NULL,"
	"studentScore int(4) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"),
}

TABLEORDER = [
    'users_students',
    'personal_info',
    'courses',
    'assignmentTypeId',
    'assignment',
]
