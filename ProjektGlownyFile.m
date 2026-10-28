%% Projekt UM - Rozpoznawanie łagodnych i złośliwych nowotworów piersi
%%Wczytanie i oddzielenie cech od etykiet
data = readtable("przetworzone-dane.xlsx");
Y = table2array(data(:, 1)); %Wydzielenie diagnozy od cech
X = table2array(data(:,2:end)); % Wydzielenie cech od diagnozy
%% Podział na zbiór uczący i testowy w proporcji 80/20
cv = cvpartition(size(X, 1), 'HoldOut', 0.2);
X_train = X(training(cv), :);
Y_train = Y(training(cv), :);
X_test = X(test(cv), :);
Y_test = Y(test(cv), :);
%% Trenowanie modelu klasyfikacyjnego
svmModel = fitcsvm(X_train, Y_train,  'KernelFunction', 'rbf','Standardize', true,  'KernelScale', 'auto');
    
    
   