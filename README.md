# LP/CP Programming Contest 2025

The traditional [LP/CP Programming Contest](https://lpcp-contest.github.io/) will be run **on site** during ICLP 2025.
It will be a two hours session, taking place on Wednesday, 17 September, from 18:00 to 20:30 (including an extra 30 minutes to accommodate any unexpected event).
The LP/CP Programming Contest 2025 will be held in person, with each team consisting of up to three participants, and is hosted at the ICLP 2025 conference venue, the University of Calabria.

**Results, stats and winner** will be announced shortly after the contest at the ICLP 2025 conference banquet.

The contest combines some features of Prolog programming contest, Answer Set Programming (ASP) Model and Solve contest, and Constraint Programming (CP) Model and Solve contest.
A variety of systems can be used in the competition, and as in the previous edition participants are not constrained to use a single system and can also combine declarative and imperative programming languages.
Submitted solutions are expected to have a declarative predominant core.

Input and output format of problems will be provided according to some easy-to-parse representation, and similarly output must be provided according to some easy-to-write format.
(Please, have a look at some [previous edition](https://github.com/lpcp-contest/lpcp-contest-2023) of the contest to get an idea of the input and output format.)


## Systems

Any declarative problem solving language or system can be used.
In particular, a Docker image where the systems

* Ciao Prolog: http://ciao-lang.org
* ECLiPSe Prolog: http://eclipseclp.org
* GNU Prolog: http://gprolog.org
* SWI-Prolog: http://www.swi-prolog.org
* XSB Prolog: http://xsb.sourceforge.net
* IDP: https://dtai.cs.kuleuven.be/pages/software/idp
* MiniZinc: http://www.minizinc.org
* Picat: http://picat-lang.org
* Potassco: https://potassco.org

are installed is available from the 2019 edition of the contest.
Details on the installation and usage of the Docker image can be found [here](https://github.com/lpcp-contest/docker-lpcpsys).

However, usage of the Docker image is optional, and other systems (as well as more recent versions of the above systems) can be run as well. When needed, we will ask for some help to run your solutions.


## Scoring

Participants will be ranked by **number of solved instances** (60 seconds timeout).
A solution is valid as soon as it does not produce wrong answers for the tested instances.

In case of an **optimization problem**, the best solution(s) for an instance provided by some participant will be awarded a point. Correct yet suboptimal answers are not considered wrong but won't receive points for the problem instance under consideration.

Ties are broken by time of the last submissions contributing some points.
Further ties are broken by cumulative execution time.

Participants will receive feedback on the number of solved instances and on errors of their submissions.
As a general suggestion, **submit solutions as soon as you have them**.


## Registration

Send an email to mario.alviano@unical.it with subject **LP/CP Programming Contest 2025 - Registration** and the following content:

* Team name;
* List of up to three participants and their affiliations;
* One or more email addresses to receive feedback.

And of course: Join us for the LP/CP Programming Contest 2025 session on **Wednesday, 17 September, from 18:00 to 20:30!**


## Submission

Via [EasyChair](https://easychair.org/conferences/?conf=iclp25).
Select the **Competition** track for the submission of solutions.

For each problem you solve, submit a ZIP archive with all files needed to run your solution.
The title must obey the following format:

```
team-name:problem-number:version
```

A good entry-point is a script like `run.sh` reading input instances from STDIN and producing output on STDOUT (see [problem-0](problem-0/example-solution-using-asp)).
If you opt for a different entry-point or different usage, provide instructions on how to execute your solution in the abstract.
We may ask support to run your solution at the end of the contest.

Keywords are not important, but you have to provide at least three of them. Use the following:

```
one
two
three
```

Please make sure that you have an EasyChair account for being ready to submit.


## Checkers

The Python client to invoke the remote checkers expects one command-line parameter, namely the problem-ID.
The instance and the solution to be checked are read from standard input.
Before the contest, the checker is restricted to an example problem.
It will be replaced to the unrestricted version during the contest.

Let us consider [problem-0](problem-0) (taken from a previous edition), and its first instance (i.e., instance-1).
If the solution to be checked is stored in file `instance.1.out`, the checker can be run with one of the following command-lines:
```bash
$ cat instance.1.in instance.1.out | ./checker.py 0 
$ cat instance.1.in instance.1.out | ./checker.py 0 --no-browser
```

The first command-line opens an ASP Chef visualization of the solution, as well as of errors (if any).
The second command-line print errors in the terminal, but needs the ASP Chef CLI (`docker pull malvi/asp-chef-cli`).

Note also that folder [problem-0](problem-0) includes an example solution using ASP.
Input is parsed with a generic Python script, which can be easily adapted to other systems.
Similarly, the output of the ASP engine is mapped to CSV by another Python script.
The entry point to execute the ASP solution is the bash script `run.sh`.


## Participants

In alphabetical order:
- **0-ASPectation**: Davide Pirrò (DeMaCS Unical Student, Italy), Emanuele Galardo (DeMaCS Unical Student, Italy), Pierpaolo Spadafora (DeMaCS Unical Student, Italy)
- **CNL Chef**: Simone Caruso (University of Genova, Italy), Mahrokh Mirani (Gran Sasso Science Institute, Italy), Luis Angel Rodriguez Reiners (University of Calabria, Italy)
- **Failure-driven Team**: Daniela Ferreiro (IMDEA Software, Spain), Marco Ciccale (IMDEA Software, Spain), Daniel Jurjo (IMDEA Software, Spain)
- **FiBoYi**: Aysu Bogatarkan (Sabanci University, Turkey), Baturay Yilmaz (Sabanci University, Turkey), Müge Fidan (Sabanci University, Turkey)
- **FrAutASP**: Alexander Beiser (TU Wien, Austria), Tobias Geibinger (TU Wien, Austria), Markus Hecher (CNRS, CRIL, France)
- **Great ASPirations**: Jesse Heyninck (Open Universiteit Heerlen, Netherlands), Veronika Semmelrock (University of Klagenfurt, Austria), Alice Tarzariol (University of Klagenfurt, Austria)
- **International Anthem**: Zach Hansen (University of Nebraska, Omaha, USA), Nicolas Rühling (University of Potsdam, Germany), Tobias Stolzmann (University of Potsdam, Germany)
- **Nduja Tapas w/ glass of Chianti**: Stefano Forti (University of Pisa, Italy), Antonio Ielo (University of Calabria, Italy), Brais Muñiz Castro (University of Coruña, Spain)
- **p**: Cristian Grozea (Fraunhofer Institute FOKUS, Berlin, Germany), Marco Gavanelli (University of Ferrara, Italy), Neng-Fa Zhou (CUNY, USA)

Participants looking for a team:
- **Mahrokh Mirani ()
  
More teams to be announced!


## Organization

- [Mario Alviano](https://alviano.net)
- [Wolfgang Faber](https://www.wfaber.com/)
