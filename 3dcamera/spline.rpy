


















































init python:
    def _spline(sp, x):
        
        
        
        
        
        N = len(sp)
        idx = -1
        h = [0]*(N-1)
        b = [0]*(N-1)
        d = [0]*(N-1)
        g = [0]*(N-1)
        u = [0]*(N-1)
        r = [0]*(N)
        
        i = 1
        while(i<N-1 and idx<0):
            if x < sp[i][0]:
                idx = i - 1
            i += 1
        
        if idx < 0:
            idx = N-2
        
        for i in range(0, N-1):
            h[i] = sp[i+1][0] - sp[i][0];
        
        for i in range(1, N-1):
            b[i] = 2.0 * (h[i] + h[i-1])
            d[i] = 3.0 * ((sp[i+1][1] - sp[i][1]) / h[i] - (sp[i][1] - sp[i-1][1]) / h[i-1])
        
        g[1] = h[1] / b[1]
        
        for i in range(2, N-2):
            g[i] = h[i] / (b[i] - h[i-1] * g[i-1])
        
        u[1] = d[1] / b[1]
        
        for i in range(2, N-1):
            u[i] = (d[i]-h[i-1] * u[i-1]) / (b[i] - h[i-1] * g[i-1])
        
        if idx > 1:
            k = idx
        else:
            k = 1
        
        r[0]   = 0.0
        r[N-1] = 0.0
        r[N-2] = u[N-2]
        
        for i in range(N-3, k, -1):
            r[i] = u[i] - g[i] * r[i+1]
        
        dx = x - sp[idx][0];
        q = (sp[idx+1][1] - sp[idx][1]) / h[idx] - h[idx] * (r[idx+1] + 2.0 * r[idx]) / 3.0
        s = (r[idx+1] - r[idx]) / (3.0 * h[idx])
        
        return sp[idx][1] + dx * (q + dx * (r[idx]  + s * dx))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
