
public class fortune {
	int a;
	fortune(int L){a=L;}
	void secret(){
	if(a<=4)
	{System.out.println(" You are ruled by a sense of duty and punctuality. You never put off doing writing a letter or doing a job\nYou never avoid doing neccessary tasks. You always finish what you have started, and never think of doing\na job you can't complete. Precise and methodical, you insiston getting a job done perfectly and on time.\nYou never consider having fun where there is work to do.");}
	else if(a>4 && a<7)
	{System.out.println(" Restless and impatient, you never stop looking for new experiences. You rarely finish a job before you start\n working on another one. You love excitement and look forward to starting new projects. Your love of\nadventure and change, oftens prevents yourself from getting involved with people. You often deny feeling love\n for people you are close to.");}
	else if(a>6 && a<9)
	{System.out.println(" You are often accused of being non-conformists and dreamers.You like wearing strange clothes and avoid\ndoing what most other people do.Criticized for being medical, you fight for your goals and have trouble\nunderstanding conservative ideas. You are deep and philosophical, and because of this, have trouble getting\nto know people.");}
	else if(a>8 && a<11)
	{System.out.println(" You are intellectual and humanists. You insist on reading only the best books and you never avoid helping\nfriends who are in trouble. You keep on telling people that humanity is basically good. People like you\n look forward to living in a peaceful world ruled by intelligence and harmony.You are true freinds, hard workers and traditionalists.");}
	else if(a>10)
	{System.out.println(" You enjoy being leaders and insist on having your own way in a group. You love taking responsibilties. You are\noften criticized for being domineering and vain and rarely admit being wrong. You are ambitious and\n never stop trying to reach your goals. Sensitive and sentimental, you can't help feeling depressed when someone hurts you.");}

	}
}
