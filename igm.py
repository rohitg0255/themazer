import PIL
import sys
from PIL import Image
import random
class Maze:
    def __init__(self,csize,height=3):
        self.osize=1
        self.csize=csize
        width=height
        self.hcells=height
        self.wcells=self.hcells
        self.cells=self.hcells*self.wcells
        self.height=(height*self.csize)+(height-1)+(2*self.osize)
        self.width=(width*self.csize)+(width-1)+(2*self.osize)
        self.img=Image.new(mode='1',size=(self.height,self.width),color=(1))
        self.pixels=self.img.load()
        self.cell_dict={}
        self.get_box()
        self.create_grid()
        self.create_cellDict()
        self.draw_maze(self.hcells)
    def get_box(self):
        for i in range(self.height):
            self.pixels[0,i]=(0)
            self.pixels[self.height-1,i]=(0)
        for i in range(self.width):
            self.pixels[i,0]=(0)
            self.pixels[i,self.width-1]=(0)
        
    def neighbours(self,i,j,ic1,ic2,k):
        if k>=ic1 and k<=ic2:
            if (k%self.wcells)==1:
                return [k+self.wcells,k-self.wcells,k+1],[0,1,2]
            elif not (k%self.wcells):
                return [k-self.wcells,k+self.wcells,k-1],[0,2,3]
            else:
                return [k-1,k+1,k-self.wcells,k+self.wcells],[0,1,2,3]
        if k>1 and k<self.wcells:
            return [k-1,k+self.wcells,k+1],[1,2,3]
        if k>self.cells-self.wcells+1 and k<self.cells:
            return [k-1,k-self.wcells,k+1],[0,1,3]
        if k==1:
            return [2,ic1-1],[1,2]
        if k==self.cells:
            return [ic2+1,k-1],[0,3]
        if k==self.wcells:
            return [k-1,2*k],[2,3]
        if k==self.cells-self.wcells+1:
            return [k+1,k-self.wcells],[0,1]
        if k==ic1-1:
            return [k+1,k+self.wcells,k-self.wcells],[0,1,2]
        if k==ic2+1:
            return [k-self.wcells,k+self.wcells,k-1],[0,2,3]
        
            
    def dfs(self,start):
        visited=[]
        print(start)
        stack=[start]
        while(stack):
            if stack[-1] not in visited:
                visited.append(stack[-1])
            top=stack[-1]
            neighbours=self.cell_dict[top][2]
            index=int(random.random()*len(neighbours))
            i=neighbours[index]
##            for i in self.cell_dict[top][2]:
            if i not in visited:
                stack.append(i)
##            j=0
            if set(neighbours).issubset(visited):
                stack.pop()
##            while(stack and set(neighbours).issubset(visited)):
####            if(stack): 
##                crop=stack[-1]
##                stack.pop()
##                neighbours=self.cell_dict[crop][2]
##                j-=1
##                visited.append(neighbours[index])
        print(visited)
        return visited

    def draw_maze(self,hcells):
        start=(int(random.random()*self.hcells))*hcells+1
        end=20+int(random.random()*self.hcells)+1
        self.maze_path=self.dfs(start)
        def helper(fro,to,l):
            xf,yf=self.cell_dict[fro][0],self.cell_dict[fro][1]
            xt,yt=self.cell_dict[to][0],self.cell_dict[to][1]
            if(fro-to==-self.hcells) or (l==2):
                for i in range(yt,yt+15):
                    self.pixels[xt-1,i]=(1)
##                print(fro,to,1)
                return 
            if(fro-to==self.hcells) or (l==0):
                for i in range(yf,yf+15):
                    self.pixels[xf-1,i]=(1)
##                print(fro,to,2)
                return
            if(fro-to==-1) or (l==1):
                for i in range(xt,xt+15):
                    self.pixels[i,yt-1]=(1)
##                print(fro,to,3)
                return
            if(fro-to==1) or (l==3):
                for i in range(xf,xf+15):
                    self.pixels[i,yf-1]=(1)
##                print(fro,to,4)
                return
    
                
        i,j=0,1
        while(j<len(self.maze_path)):
            from_,to_=self.maze_path[i],self.maze_path[j]
            neighbours2,neighbours3=self.cell_dict[to_][2],self.cell_dict[to_][3]
            if  set(neighbours2).issubset(self.maze_path[:j]):
                l=neighbours3[int(random.random()*len(neighbours3))]
                helper(from_,to_,l)
            else:
                helper(from_,to_,4)
            i+=1
            j+=1
        print(j)
##            self.img.show()
        self.img.save('pill.png')       
        

            
    def create_cellDict(self):
        i,j,k=1,1,1
        ic1,ic2=self.wcells+2,self.cells-self.wcells-1
        while( i<=self.height-1-self.csize):
            while(j<=self.width-1-self.csize):
                n,l=self.neighbours(i,j,ic1,ic2,k)
##                print(k,n,l)
                self.cell_dict[k]=[i,j,n,l]
                j+=16
                k+=1
            j=1
            i+=16

    def create_grid(self):
        j=16
        for i in range(1,self.height):
           while(j<self.width-1-15):
               self.pixels[i,j]=(0)
               self.pixels[j,i]=(0)
               j+=16
           j=16
        
M=Maze(15,6)












