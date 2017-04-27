data = read.table("/Users/xinyin/Desktop/data.txt")
names(data) <- c("SeriesA","SeriesB","SeriesC","Location","Employees","MarketType")
A<-data$SeriesA
B<-data$SeriesB
C<-data$SeriesC
I1<-c()
I2<-c()
I3<-c()
l<-length(A)
for (i in 1:l){
	i1<-(B[i]/A[i])-1
	i2<-(C[i]/B[i])-1
	i3<-(C[i]/A[i])-1
	I1<-c(I1,i1)
	I2<-c(I2,i2)
	I3<-c(I3,i3)

}
C1<-c()
C2<-c()
C3<-c()
for (i in 1:l){
	if (I1[i]>1){
		C1<-c(C1,1)
	}
	else{
		C1<-c(C1,0)
}
	if (I2[i]>1){
		C2<-c(C2,1)
	}
	else{
		C2<-c(C2,0)
}
	if (I3[i]>2){
		C3<-c(C3,1)
	}
	else{
		C3<-c(C3,0)
}
}
data$C1<-C1
data$C2<-C2
data$C3<-C3

lm1<-lm(I1~Location+Employees+MarketType,data=data)
lm2<-lm(I2~Location+Employees+MarketType,data=data)
lm3<-lm(I3~Location+Employees+MarketType,data=data)
