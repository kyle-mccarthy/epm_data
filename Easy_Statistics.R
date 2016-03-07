average_exams_by_intermediate = read.csv("/Users/muitprogram/Desktop/Kyle-Data/average_exam_grades_by_intermediate_scores.csv")  # read csv file

average_exams_by_intermediate = subset(average_exams_by_intermediate, select=c("student_id", "ex_2_es_4_1", "ex_2_es_6_1", "ex_2_es_6_2", "averageIntermediateScore", "averageExamScore", "bestExamScore", "letterGrade"))
naiveBayess = subset(average_exams_by_intermediate, select=c("ex_2_es_4_1", "ex_2_es_6_1", "ex_2_es_6_2", "averageIntermediateScore", "letterGrade"))

library(ggplot2)

ggplot(average_exams_by_intermediate, aes(x=ex_2_es_6_2, y=averageExamScore, xmin=0, ymin=0)) +
  geom_point(shape=1)+
  scale_x_continuous( expand = c(0,0) , limits = c(0,6) )+
  scale_y_continuous( expand = c(0,0), limits = c(0,35) )

#install.packages("alr3")
library(alr3)
M.lm=lm(averageIntermediateScore~bestExamScore,data=average_exams_by_intermediate)
#Here you will see the R square value
str(summary(M.lm))

#install.packages('e1071', dependencies = TRUE)
library(e1071)
library(class) 
summary(average_exams_by_intermediate)

### This example works as well
#classifier<-naiveBayes(naiveBayes[,-5], naiveBayes[,5])
classifier<-naiveBayes(letterGrade ~ ., data=naiveBayess)
table(predict(classifier, naiveBayess[,-5]), naiveBayess[,5])

### Examples from Slides which works and prints out the table
install.packages("klaR")
install.packages("caret")

library("klaR")
library("caret")

x = naiveBayess[,-5]
y = naiveBayess$letterGrade

model = train(x,y,'nb',trControl=trainControl(method='cv',number=10))
predict(model$finalModel,x)$class
table(predict(model$finalModel,x)$class,y)


### NOT SURE WHAT THIS DOES  
#install.packages('ElemStatLearn')
library('ElemStatLearn')

sub = sample(nrow(spam), floor(nrow(spam) * 0.9))
train = spam[sub,]
test = spam[-sub,]

xTrain = train[,-58]
yTrain = train$spam

xTest = test[,-58]
yTest = test$spam

model = train(xTrain,yTrain,'nb',trControl=trainControl(method='cv',number=10))
prop.table(table(predict(model$finalModel,xTest)$class,yTest))
