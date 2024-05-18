import java.util.ArrayList;
import java.util.Scanner;

class Student {
    private int id;
    private String name;
    private String gender;
    private String birthDate;
    private String mobileNumber;
    private String address;

    public Student(int id, String name, String gender, String birthDate, String mobileNumber, String address) {
        this.id = id;
        this.name = name;
        this.gender = gender;
        this.birthDate = birthDate;
        this.mobileNumber = mobileNumber;
        this.address = address;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getGender() {
        return gender;
    }

    public String getBirthDate() {
        return birthDate;
    }

    public String getMobileNumber() {
        return mobileNumber;
    }

    public String getAddress() {
        return address;
    }
}



public class StudentManagementSystem {
    public static void addStudent(ArrayList<Student> students) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter student ID: ");
        int id = scanner.nextInt();
        scanner.nextLine(); // consume newline character
        System.out.print("Enter student name: ");
        String name = scanner.nextLine();
        System.out.print("Enter student gender (M/F): ");
        String gender = scanner.nextLine();
        System.out.print("Enter student birth date (YYYY-MM-DD): ");
        String birthDate = scanner.nextLine();
        System.out.print("Enter student mobile number: ");
        String mobileNumber = scanner.nextLine();
        System.out.print("Enter student address: ");
        String address = scanner.nextLine();

        for (Student student : students) {
            if (student.getName().equals(name)) {
                System.out.println("Student with this name already exists.");
                return;
            }
        }

        students.add(new Student(id, name, gender, birthDate, mobileNumber, address));
        System.out.println("Student added successfully.");
    }

    public static void removeStudent(ArrayList<Student> students) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter student ID to remove: ");
        int id = scanner.nextInt();

        for (Student student : students) {
            if (student.getId() == id) {
                students.remove(student);
                System.out.println("Student removed successfully.");
                return;
            }
        }

        System.out.println("Student not found.");
    }

    public static void displayStudents(ArrayList<Student> students) {
        System.out.println("ID\tName\t\tGender\tBirth Date\tMobile Number\tAddress");
        for (Student student : students) {
            String title = "";
            if (student.getGender().equals("M")) {
                title = "Mr.";
            } else if (student.getGender().equals("F")) {
                title = "Mrs.";
            }
            System.out.printf("%d\t%s %s\t%s\t%s\t%s\t%s\n",
                    student.getId(), title, student.getName(), student.getGender(),
                    student.getBirthDate(), student.getMobileNumber(), student.getAddress());
        }
    }
		
    public static void main(String[] args) {
        ArrayList<Student> students = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\n1. Add Student");
            System.out.println("2. Remove Student");
            System.out.println("3. Display All Students");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            String choice = scanner.nextLine();

            switch (choice) {
                case "1":
                    addStudent(students);
                    break;
                case "2":
                    removeStudent(students);
                    break;
                case "3":
                    displayStudents(students);
                    break;
                case "4":
                    System.out.println("Exiting program.");
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
		}      }
        }
    }
}

