import { defineConfig } from 'vocs/config'
import generatedSidebar from './generated/sidebar.json'

type SidebarItem = {
  text: string
  link?: string
  items?: SidebarItem[]
}

const apiReference = generatedSidebar.apiReference as SidebarItem
const tlReference = generatedSidebar.tlReference as SidebarItem

export default defineConfig({
  rootDir: '.',
  title: 'sent',
  description: 'Async MTProto client library for Telegram user accounts and bots',
  sidebar: [
    { text: 'Introduction', link: '/introduction' },
    {
      text: 'Getting Started',
      items: [
        { text: 'Installation', link: '/getting-started' },
        { text: 'Authentication', link: '/guides/authentication' },
      ],
    },
    {
      text: 'Guides',
      items: [
        { text: 'Build with AI', link: '/guides/ai' },
        { text: 'Bot', link: '/guides/bot' },
        { text: 'User account', link: '/guides/user-account' },
        { text: 'Conversation', link: '/guides/conversation' },
        { text: 'Entities', link: '/guides/entities' },
        { text: 'Events', link: '/guides/events' },
        { text: 'Media & Files', link: '/guides/media' },
        { text: 'Inline Keyboards', link: '/guides/keyboards' },
        { text: 'Error Handling', link: '/guides/error-handling' },
        { text: 'Proxy & Transport', link: '/guides/proxy' },
        { text: 'Raw TL RPC', link: '/guides/raw-tl' },
      ],
    },
    apiReference,
    tlReference,
    { text: 'Development', link: '/development' },
  ],
  socials: [{ icon: 'github', link: 'https://github.com/kalanakt/sent' }],
  editLink: {
    link: 'https://github.com/kalanakt/sent/edit/main/docs/src/pages/:path',
  },
})
