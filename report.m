fileID = fopen('data.csv');
C = textscan(fileID,'%s %s %q %q %q %q %s %s %s %s','Delimiter',',');
fclose(fileID);
whos C

l = length(C{1});

for i = 3:6
    for j = 1:l
       a = C{i}{j};
      
       if isempty(a)
           C{i}{j} = 0;
       elseif strcmp(a,'Unknown')
           C{i}{j} = 0;
       else
           a = a(2:end);
           a1 = str2double(a);
           C{i}{j} = a1;
       end
    end
end

A = [];
%index of employee 
for i = 9
    for j = 1:l
        if isempty(C{i}{j})
            A = A;
        else
           A = [A;j];
        end
   end
end
% market 
M = [];
A10 = [];
L = [];
for i = 10
    for j = 1:l
        if isempty(C{i}{j})
            A10 = A10;
        else
           market = textscan(C{10}{j},'%s','delimiter',';');
           M = [M;market{:}];
           L =[L;length(market{:})];
           A10 = [A10;j];
        end
   end
end
M1 = unique(M);
M1C = M1Copy;
idxsM = arrayfun(@(x)find(strcmp(M1,x),1),M);
CM = [];
ii = 1; 
for j = 1:length(A10)
    CC = [];
    for l1 = 1: L(j)
        CC = [CC;M1Copy(idxsM(ii),2)];
        ii = 1 + ii;
    end
    CM = [CM;mode(cell2mat(CC))];
end
Names1 = {'Financial','Consumer Services','Industry','Technology','Cosumer Goods','Health Care','Basic Material','Energy','Education'};
%C = categorical(CM,[1:length(Names1)],Names1);
%histogram(C);
           
        
%S1 = cell(length(A),2);
S1 = [];
S2 = [];
S3 = [];
S4 = [];
S5 = [];
S5 = [];
S6 = [];
for j = 1:length(A10)
    S1 = [S1;C{3}{A10(j)}];
    %S2 = [S2;cellstr(C{10}{A10(j)})];
    %Series A
    S3 = [S3;C{4}{A10(j)}];
    %Series B
    S4 = [S4;C{5}{A10(j)}];
    %Series C 
    S5 = [S5;C{6}{A10(j)}];
    % Total Fund
    S6 = [S6;C{3}{A10(j)}+C{4}{A10(j)}+C{5}{A10(j)}+C{6}{A10(j)}];
end 
%Names = unique(S2);
%idxs = arrayfun(@(x)find(strcmp(Names,x),1),S2);
Value1 = zeros(4,1);
Value2 = zeros(4,1);
Value3 = zeros(4,1);
Number = zeros(4,1);
for i = 1:length(A10)
    if CM(i) == 1
        Value1(1,1) = Value1(1,1) + S3(i,1);
        Value2(1,1) = Value2(1,1) + S4(i,1);
        Value3(1,1) = Value3(1,1) + S5(i,1);
        Number(1,1) = Number(1,1) + 1;
    end
    if CM(i) == 2
        Value1(2,1) = Value1(2,1) + S3(i,1);
        Value2(2,1) = Value2(2,1) + S4(i,1);
        Value3(2,1) = Value3(2,1) + S5(i,1);
        Number(2,1) = Number(2,1) + 1;
    end
    if CM(i) == 3
        Value1(3,1) = Value1(3,1) + S3(i,1);
        Value2(3,1) = Value2(3,1) + S4(i,1);
        Value3(3,1) = Value3(3,1) + S5(i,1);
        Number(3,1) = Number(3,1) + 1;
    end
     if CM(i) == 4
        Value1(4,1) = Value1(4,1) + S3(i,1);
        Value2(4,1) = Value2(4,1) + S4(i,1);
        Value3(4,1) = Value3(4,1) + S5(i,1);
        Number(4,1) = Number(4,1) + 1;
     end
end
Ave1 = zeros(1,4);
Ave2 = zeros(1,4);
Ave3 = zeros(1,4);
for i = 1:4
    Ave1(1,i) = double(Value1(i,1)/Number(i,1));   
    Ave2(1,i) = double(Value2(i,1)/Number(i,1));   
    Ave3(1,i) = double(Value3(i,1)/Number(i,1));   

end
%C = categorical(idxs,[1:length(Names)],Names);
%histogram(C);
Matrix = [];
E1 = [];
E2 = [];
E3 = [];
E4 = [];
E5 = [];
for j = 1:length(A10)
    %S1 = [S1;C{3}{A10(j)}];
    %S2 = [S2;cellstr(C{10}{A10(j)})];
    %Series A
    E1 = [E1;C{4}{A10(j)}];
    %Series B
    E2 = [E2;C{5}{A10(j)}];
    %Series C 
    E3 = [E3;C{6}{A10(j)}];
    %Location
    E4 = [E4;cellstr(C{7}{A10(j)})];
    %Employee
    E5 = [E5;cellstr(C{9}{A10(j)})];
end 

