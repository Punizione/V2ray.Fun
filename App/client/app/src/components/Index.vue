<template>
  <v-container fluid>
      <v-layout column>
        <v-card>
          <v-container fluid grid-list-md>
            <v-layout row wrap>
              <v-flex xs12>
                <v-list two-line>
                <v-list-tile>
                  <v-flex xs6>
                    {{ nameFormat('status') }}
                  </v-flex>
                  <v-flex xs6>
                    <v-chip v-if="status" color="green" text-color="white">
                      <v-avatar class="green darken-4">
                        <v-icon>check_circle</v-icon>
                      </v-avatar>
                      {{ nameFormat('server-on') }}
                    </v-chip>
                    <v-chip v-else color="green" text-color="white">
                      <v-avatar class="green darken-4">
                        <v-icon>check_circle</v-icon>
                      </v-avatar>
                      {{ nameFormat('server-off') }}
                    </v-chip>
                  </v-flex>
                </v-list-tile>
                <v-list-tile v-for="(item,index) in configs" :key="index">
                  <v-flex xs6 >
                    {{ nameFormat(item.name) }}
                  </v-flex>
                  <v-flex xs5>
                    {{ item.value }}
                  </v-flex>
                  <v-flex xs1>
                    <v-btn flat icon>
                      <v-icon v-if="copyAble(item.name)">filter_none</v-icon>
                    </v-btn>
                  </v-flex>

                </v-list-tile>
               
                <v-list-tile v-if='protocol === "vmess"'>
                  <v-flex xs6>
                    {{ nameFormat('uuid') }}
                  </v-flex>
                  <v-flex xs5>
                    {{ uuid }}
                    <v-spacer></v-spacer>
                  </v-flex>
                  <v-flex xs1>
                    <v-btn flat icon>
                      <v-icon>filter_none</v-icon>
                    </v-btn>
                  </v-flex>
                </v-list-tile>
                <v-list-tile v-if='protocol === "mtproto"'>
                  <v-flex xs6>
                    {{ nameFormat('secret') }}
                  </v-flex>
                  <v-flex xs5>
                    {{ secret }}
                  </v-flex>
                  <v-flex xs1>
                    <v-btn flat icon>
                      <v-icon>filter_none</v-icon>
                    </v-btn>
                  </v-flex>
                </v-list-tile>
                 <v-list-tile>
                  <v-flex xs6>
                    {{ nameFormat('tls') }}
                  </v-flex>
                  <v-flex v-if='tls' xs6>
                    <v-icon>check</v-icon>
                    {{ nameFormat('on') }}
                  </v-flex>
                  <v-flex v-else xs6>
                    <v-icon>check</v-icon>
                    {{ nameFormat('off') }}
                  </v-flex>
                </v-list-tile>
                <v-list-tile>
                  <v-flex xs6>
                    {{ nameFormat('mux') }}
                  </v-flex>
                  <v-flex v-if='mux' xs6>
                    <v-icon>check</v-icon>
                    {{ nameFormat('on') }}
                  </v-flex>
                   <v-flex v-else xs6>
                    <v-icon>check</v-icon>
                    {{ nameFormat('off') }}
                  </v-flex>
                </v-list-tile>
                
              </v-list>
              </v-flex>
              
            </v-layout>
          </v-container>
        </v-card>   

      </v-layout>
      <v-snackbar
        v-model="snackbar"
        bottom
        :timeout="alertTimeout"
      >
        {{ alertText }}
      </v-snackbar>
  </v-container>
</template>

<script>
  export default {
    data: () => ({
      tls: false,
      status: false,
      domain: "none",
      encrypt: "auto",
      uuid: "65dae0e3-ef4a-4b75-8507-6c99a8fdf8a6",
      ip: "",
      mux: false,
      secret: "969957b6274f7c765812aebf1fa759f5",
      protocol: "vmess",
      trans: "tcp",
      port: 4617,

      snackbar: false,
      alertText: '',
      alertTimeout: 2000,

      configs: [
        { 'name': 'domain', 'value': 'none' },
        { 'name': 'encrypt', 'value': 'auto' },
        { 'name': 'ip', 'value': '' },
        { 'name': 'protocol', 'value': 'vmess' },
        { 'name': 'trans', 'value': 'tcp' },
        { 'name': 'port', 'value': 4617 }

      ],

      formatMap: {
        'port': '端口',
        'mux': '多路复用',
        'trans': "传输层协议",
        'domain': '域名',
        'encrypt': '加密方法',
        'uuid': 'UUID',
        'ip': 'IP',
        'secret': '用户秘钥',
        'protocol': '协议',
        'status': '状态',
        'tls': 'TLS',
        'server-on': '运行中',
        'server-off': '停止',
        'on': '已开启',
        'off': '已关闭'
      },
      copyArray: [
        'domain', 'uuid', 'secret', 'ip'
      ],
      message: {
        'request_fail': "请求失败"
      }
    }),
    methods: {
      copyAble(item) {
        if ( this.copyArray.indexOf(item) != -1 ) {
          return true
        } else {
          return false
        }
      },
      nameFormat(item) {
        return this.formatMap[item]
      },
      fetchData() {
        this.configs = {}
        this.loaded = false
        this.axios.get('/api/get_info').then((response) => {
          if (response.status == 200) {
            let retData = response.data
            this.tls = retData['tls']
            this.status = retData['status']
            this.mux = retData['mux']
            this.config['port'] = retData['port']
            this.configs['ip'] = retData['ip']
            let protocol = this.configs['protocol'] = retData['protocol']
            if ( protocol === 'vmess' ) {
              this.configs['uuid'] = retData['uuid']
              this.configs['encrypt'] = retData['encrypt']
            } else if ( protocol === 'mtproto' ) {
              this.configs['secret'] = retData['secret']
            }
            this.configs['trans'] =  retData['trans']
            this.configs['domain'] = retData['domain']
            
          }
        }).catch(err => { 
          this.loaded = true
          this.alertText = this.message['request_fail']
          this.snackbar = true
          console.log(err)
        })
      }
    },
    created() {
      // this.fetchData()
      this.configs= [
        { 'name': 'domain', 'value': 'none' },
        { 'name': 'encrypt', 'value': 'auto' },
        { 'name': 'ip', 'value': '' },
        { 'name': 'protocol', 'value': 'vmess' },
        { 'name': 'trans', 'value': 'tcp' },
        { 'name': 'port', 'value': 4617 }

      ]
    },
    name: 'Index'
  }
</script>