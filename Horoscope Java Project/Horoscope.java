import java.util.*;
public class Horoscope {
	public static void main(String args[]) {
while(true) {
			
System.out.println("\t_____________HOROSCOPE_______________\n");
System.out.println("\tWHAT COMPUTER THINKS ABOUT YOU...!!!!!!!!\n");
Scanner sc=new Scanner(System.in);

System.out.println("\tENTER YOUR DETAILS\n");
System.out.print("NAME :  ");
String name=sc.nextLine();
char gender;
while(true)
{
 System.out.print("Gender (M/F) : ");
 gender=sc.next().charAt(0);  
 
 if(gender=='M' || gender=='m' || gender=='F'  || gender=='f')
 {
   break;
 }   
 else
 {
  System.out.print("***Specify your GENDER Correctly!***\n"); 
 }
}
int month;
while(true)
{
 System.out.print("Month you were born (1-12) : ");
 month=sc.nextInt();

 if(month>=1 && month<=12)
 {
   break;
 }   
 else
 {
  System.out.println("***Invalid Month!.   Enter Again.***"); 
 }
}
int date;
System.out.print("Enter Your Date Of Birth : ");
date=sc.nextInt();
int fav_no;
while(true)
{
 System.out.print("Favourite Number(1-10) : ");
 fav_no=sc.nextInt();

 if(fav_no>=1 && fav_no<=10)
 {
   break;
 }   
 else
 {
  System.out.println("***Not In The Range Btw 1 to 10.   Enter Again!***"); 
 }
}
int name_lnth=name.length();


System.out.println("\n\tHere's Your Horoscope......");

System.out.println("\nStar-Birth/Zodiac Sign :-\n");
star st1=new star(date,month);
st1.zodiac();
System.out.println("\nYour Cartoon Personality :-\n");
personality pe1=new personality(gender,fav_no);
pe1.cartoon();
System.out.println("\nYour Ancient Ancestor :-\n");
ancestor an1=new ancestor(fav_no,month);
an1.ancient();
System.out.println("\nYour Special Ability :-\n");
ability ab1=new ability(month,fav_no);
ab1.special();
System.out.println("\nYour Celebrity Crush:-\n");
celebrity ce1=new celebrity(gender,month);
ce1.crush();
System.out.println("\nSecret In Your Name :-\n");
fortune fo1=new fortune(name_lnth);
fo1.secret();

System.out.println("\nPress Any key To Continue.\n(To Exit Press:'N') ");
char x=sc.next().charAt(0);
if(x=='n' || x=='N')
	{System.out.println("\nTHANK YOU");
	break;}
}
}
}
