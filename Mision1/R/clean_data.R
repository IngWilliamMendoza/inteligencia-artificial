# dataset = read.csv('../Data_sets/Data.csv')
# 
# # Tratamiento del los valores NA
# dataset$Age = ifelse(is.na(dataset$Age), 
#                      ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
#                      dataset$Age)
# 
# dataset$Salary = ifelse(is.na(dataset$Salary), 
#                      ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
#                      dataset$Salary)
# 
# dataset$Salary = ifelse(is.na(dataset$Salary), 
#                         ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
#                         dataset$Salary)

file.exists("../Data_sets/Data.csv")
