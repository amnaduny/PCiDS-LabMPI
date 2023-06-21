from mpi4py import MPI

comm = MPI.COMM_WORLD
worker = comm.Get_rank() # Rank
size = comm.Get_size()

initial  = 2
if(worker == 0):
    print('size : ', size)
    comm.send(initial, dest=worker+1)
elif worker == size - 1:
    rec = comm.recv(source=worker-1)
    print("receive : ",rec*2)
else:
    rec = comm.recv(source=worker-1)
    comm.send(rec*2, dest=worker+1)
    print("worker : {0}, receive : {1}".format(worker, rec))
