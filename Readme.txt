pyABA Math
	This is a gnu/linux variation of ABA Math, developed by Harry Dolan, father of an eight-year-old autistic boy. 
[  Quoting from http://abamath.sourceforge.net/   ]
Applied Behavioral Analysis (ABA) therapy, has been used successfully by Lovaas, et. al., to treat young autistic children.

ABA Therapy Overview
	ABA therapy breaks each learning task into several (sometimes many) sub-tasks. For example, to teach a student the task of writing a mark on a piece of paper may require that he first be taught the sub-tasks of picking up a pencil, locating the pointed end, holding the piece of paper, running the point of the pencil against the paper, etc. The number and complexity of sub-tasks will vary with each student. 
	Each sub-task is taught separately using (sometimes many) Discrete Trials wherein the student is asked (once) to perform the task. Only after he has done it correctly a certain number of times, and without assistance from the therapist, is the sub-task considered mastered. Then the program moves on to the next sub-task. 
	ABA therapy is also characterized by data. The therapists keep records on the results of each trial, for each sub-task, of each task the student is taught. Performance is therefore easily quantified. ABA therapy generates a lot of data. 
Stages of Descrete Trial Teaching
Mass Trial (MT): Same Sd given each trial, with only one choice offered, e.g., "Touch pencil", when a pencil is the only item on the table. 
Distractor Trial (DT): Same Sd given each trial, with several choices offered, e.g., "Touch pencil", with a pencil and two other "distractor" items on the table. 
Random Rotation (RR): Similar to DT, but the other items are previously mastered items, and the Sd is usually for the aquisition item but is sometimes for one of the others. 
Review: A random testing of previously mastered items. 
How pyABA Math tries to use these methods
	ABA Math uses four stages(seven internally) for each acquisition item, three receptive and four expressive. The aquisition item is a single math fact such as "1+2=3". At each stage the student must answer correctly a number of times before going on to the next stage.

Level 1 
MT-receptive: Acquisition item (AI) in one of three random locations. Student asked to click on it. 
Level 2
DT-receptive: AI + 2 distractors. Student asked to click AI. 
RR-receptive: AI + 2 Mastered items. Student asked to click one (AI about half the time).
Level 3
MT-expressive: AI problem + AI answer in random locations. Student asked to click answer. 
DT-expressive: AI problem, AI + 2 distractor answers. Student asked to click answer. 
Level 4
RR-expressive: AI or MI (AI about half the time) + 10 answers. Student to click answer. 
Review: Either AI or MI randomly chosen, 10 answers. Student to click answer. 
	
	After each correct response the student is praised with a verbal "good job!" After each completed stage he is rewarded with a pleasing star. Whenever the student fails to response within a set time , he is prompted with a flashing border around the correct item. 

 
