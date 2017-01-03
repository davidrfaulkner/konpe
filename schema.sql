-- Schema for konpe

create table Tournaments (
    TournamentID    integer primary key autoincrement not null,
    InsertDate      date DEFAULT CURRENT_TIMESTAMP,
    TournamentName  text,
    TournamentDate  text,
    TournamentLocation  text,
    TournamentRings  integer
);

create table Participants (
    ParticipantID   integer primary key autoincrement not null,
    TournamentID    integer not null,
    InsertDate      date DEFAULT CURRENT_TIMESTAMP,
    FirstName       text,
    LastName        text,
    TeamName        text,
    Age             text,
    Gender          text,
    Grade           integer,
    GradeReadable   text,
    Dojo            text,
    Region          text,
    Country         text,
    Kata            boolean,
    Kumite          boolean,
    TeamKata        text,
    TeamKumite      text,
    Assigned        boolean,
    WasMoved        boolean
);

create table TeamMemberships (
    TeamMembershipID  integer primary key autoincrement not null,
    TournamentID      integer not null,
    ParticipantID     integer not null,
    InsertDate      date DEFAULT CURRENT_TIMESTAMP,
    TeamName          text,
    FirstName         text,
    LastName          text
);

create table Winners (
    WinnerID  integer primary key autoincrement not null,
    TournamentID    integer not null,
    ParticipantID   integer not null,
    DivisionID      integer not null,
    InsertDate      date DEFAULT CURRENT_TIMESTAMP,
    TeamName        text,
    FirstName       text,
    LastName        text,
    Placing         text,
    Dojo            text,
    Region          text,
    Country         text
);

create table Divisions (
    DivisionID      integer primary key autoincrement not null,
    TournamentID    integer not null,
    InsertDate      date DEFAULT CURRENT_TIMESTAMP,
    Division        text,
    MinGrade        integer,
    MaxGrade        integer,
    TeamDivision    boolean,
    Gender          text
);

create table DivisionParticipants (
  DivisionParticipantID   integer primary key autoincrement not null,
  TournamentID            integer not null,
  InsertDate              date DEFAULT CURRENT_TIMESTAMP,
  ParticipantID           integer,
  TeamMembershipID        integer,
  WasMoved                boolean,
  FirstName               text,
  LastName                text,
  Region                  text,
  Dojo                    text,
  Grade                   text,
  GradeReadable           text
);

create table Config (
  Key        text primary key,
  Value      text
);

insert into Config
values ('Dojos','JSON');

insert into Config
values ('Grades','JSON');

insert into Config
values ('Countries','JSON');

insert into Config
values ('Regions','JSON');
