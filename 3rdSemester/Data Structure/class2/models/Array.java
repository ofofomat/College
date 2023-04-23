package models;
import java.util.Arrays;

public class Array {
    private Student[] students = new Student[100];
    private int totalStudents = 0;

    public void addStudent(Student student){
        checkSpace();
		this.students[this.totalStudents] = student;
		this.totalStudents++;
    }

    private void checkSpace() {
		if (this.totalStudents == this.students.length) {
			Student[] newStudents = new Student[students.length * 2];
			for (int i = 0; i < students.length; i++) {
				newStudents[i] = this.students[i];
			}
			this.students = newStudents;
		}
	}
    public void addStudent(int position, Student student){
        checkSpace();
		if (position <= this.totalStudents)
			for (int i = this.totalStudents - 1; i >= position; i--) {
				this.students[i + 1] = this.students[i];
			}
		this.students[position] = student;
		this.totalStudents++;
    }
    public Student catchStudent(int position){
        if (position <= this.totalStudents)
			return this.students[position];
		return null;
    }
    public void removeStudent(int position){
        if (position <= this.totalStudents)
			for (int i = position; i < this.totalStudents - 1; i++) {
				this.students[i] = this.students[i + 1];
			}
		this.totalStudents--;
    }
    public boolean thereIs(Student student){
        if (student != null) {
			for (int i = 0; i < this.totalStudents; i++) {
				if (student.equals(students[i])) {
					return true;
				}
			}
		}
		return false;
    }
    public int size(){
        return this.totalStudents;
    }

    @Override
    public String toString(){
        return Arrays.toString(students);
    }
}
