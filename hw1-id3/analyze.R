

sme <- function()
{
    setwd("/Users/junhe/workdir/cs760hw/machine-learning/hw1-id3/")
    source("./analyze.R")
}


read.file <- function(fname)
{
    d = read.table(file=fname,
                   header=T)
    return(d)
}

entropy <- function(d)
{
    d = as.data.frame(table(d$class))
    v = d$Freq
    v = v[v!=0]
    v = v/sum(v)
    ret = sum(v * log2(v))
    #cat('ret', -ret, '\n')
    return(-ret)
}

infogain <- function(d, attr)
{
    entropy.S = entropy(d)
    
    prob = as.data.frame(table(d[,attr]))
    prob$p = prob$Freq/sum(prob$Freq)
    #print(prob)

    d2 = ddply(d, attr, entropy)

    entropy.Right = sum(prob$p * d2$V1)
    gain = entropy.S - entropy.Right
    #print(gain)
    return (gain)
}


part2.analysis <- function(d)
{
    print(head(d))
    d$accuracy = with(d, goodprediction/total)

    ddstats <- function(d) {
        mmin = min(d$accuracy)
        mmax = max(d$accuracy)
        aavg = mean(d$accuracy)

        return(data.frame(min=mmin,
                          max=mmax,
                          avg=aavg))
    }
    dd = ddply(d, .(trainratio), ddstats)
    dd = melt(dd, id=c('trainratio'))
    print(dd)
    p <- ggplot(dd, aes(x=trainratio, y=value, color=variable)) +
         geom_line() +
         geom_point() +
         xlab('traning ratio') +
         ylab('accuracy')
    print(p)
}

part3.analysis <- function(d)
{
    d$accuracy = with(d, goodprediction/total)
    p <- ggplot(d, aes(x=m, y=accuracy)) +
         geom_point() +
         geom_line()
    print(p)
}

main <- function()
{
    #d <<- read.file('./heart_train.table')
    #print(d)
    #print (entropy(d))
    #infogain(d, 'exang')
    #infogain(d, 'thal')

    #d = read.file('./part2.data.heart.txt')
    #part2.analysis(d)

    #d = read.file('./part2.data.diabetes.txt')
    #part2.analysis(d)

    #d = read.file('./part3.data.heart.txt')
    #part3.analysis(d)

    d = read.file('./part3.data.diabetes.txt')
    part3.analysis(d)
}

main()

