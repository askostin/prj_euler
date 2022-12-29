sum <- 0
n3 <- 1
n5 <- 1
for (i in 1:999) {
  n3 <- ifelse(n3 == 3, 1, n3 + 1)
  n5 <- ifelse(n5 == 5, 1, n5 + 1)
  if (n3 == 1 | n5 == 1) {
    sum <- sum + i
  }
}
print(sum)

# answer is 233168