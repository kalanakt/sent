// deno-fmt-ignore-file
// biome-ignore format: generated types do not need formatting
// prettier-ignore
import type { PathsForPages } from 'waku/router'

// prettier-ignore
type Page =
  | { path: '/api/client/auth'; render: 'static' }
  | { path: '/api/client/bots'; render: 'static' }
  | { path: '/api/client/chats'; render: 'static' }
  | { path: '/api/client/connection'; render: 'static' }
  | { path: '/api/client/dialogs'; render: 'static' }
  | { path: '/api/client/files'; render: 'static' }
  | { path: '/api/client'; render: 'static' }
  | { path: '/api/client/messages'; render: 'static' }
  | { path: '/api/client/updates'; render: 'static' }
  | { path: '/api/client/users'; render: 'static' }
  | { path: '/api/errors'; render: 'static' }
  | { path: '/api/events/album'; render: 'static' }
  | { path: '/api/events/callbackquery'; render: 'static' }
  | { path: '/api/events/chataction'; render: 'static' }
  | { path: '/api/events'; render: 'static' }
  | { path: '/api/events/inlinequery'; render: 'static' }
  | { path: '/api/events/messagedeleted'; render: 'static' }
  | { path: '/api/events/messageedited'; render: 'static' }
  | { path: '/api/events/messageread'; render: 'static' }
  | { path: '/api/events/newmessage'; render: 'static' }
  | { path: '/api/events/raw'; render: 'static' }
  | { path: '/api/events/userupdate'; render: 'static' }
  | { path: '/api/helpers/button'; render: 'static' }
  | { path: '/api/helpers/conversation'; render: 'static' }
  | { path: '/api/sessions'; render: 'static' }
  | { path: '/development'; render: 'static' }
  | { path: '/getting-started'; render: 'static' }
  | { path: '/guides/ai'; render: 'static' }
  | { path: '/guides/authentication'; render: 'static' }
  | { path: '/guides/bot'; render: 'static' }
  | { path: '/guides/conversation'; render: 'static' }
  | { path: '/guides/entities'; render: 'static' }
  | { path: '/guides/error-handling'; render: 'static' }
  | { path: '/guides/events'; render: 'static' }
  | { path: '/guides/keyboards'; render: 'static' }
  | { path: '/guides/media'; render: 'static' }
  | { path: '/guides/proxy'; render: 'static' }
  | { path: '/guides/raw-tl'; render: 'static' }
  | { path: '/guides/user-account'; render: 'static' }
  | { path: '/'; render: 'static' }
  | { path: '/introduction'; render: 'static' }
  | { path: '/tl/functions/account'; render: 'static' }
  | { path: '/tl/functions/aicompose'; render: 'static' }
  | { path: '/tl/functions/auth'; render: 'static' }
  | { path: '/tl/functions/bots'; render: 'static' }
  | { path: '/tl/functions/channels'; render: 'static' }
  | { path: '/tl/functions/chatlists'; render: 'static' }
  | { path: '/tl/functions/contacts'; render: 'static' }
  | { path: '/tl/functions/folders'; render: 'static' }
  | { path: '/tl/functions/fragment'; render: 'static' }
  | { path: '/tl/functions/help'; render: 'static' }
  | { path: '/tl/functions/langpack'; render: 'static' }
  | { path: '/tl/functions/messages'; render: 'static' }
  | { path: '/tl/functions/mtproto'; render: 'static' }
  | { path: '/tl/functions/payments'; render: 'static' }
  | { path: '/tl/functions/phone'; render: 'static' }
  | { path: '/tl/functions/photos'; render: 'static' }
  | { path: '/tl/functions/premium'; render: 'static' }
  | { path: '/tl/functions/smsjobs'; render: 'static' }
  | { path: '/tl/functions/stats'; render: 'static' }
  | { path: '/tl/functions/stickers'; render: 'static' }
  | { path: '/tl/functions/stories'; render: 'static' }
  | { path: '/tl/functions/updates'; render: 'static' }
  | { path: '/tl/functions/upload'; render: 'static' }
  | { path: '/tl/functions/users'; render: 'static' }
  | { path: '/tl'; render: 'static' }
  | { path: '/tl/types/account'; render: 'static' }
  | { path: '/tl/types/aicompose'; render: 'static' }
  | { path: '/tl/types/auth'; render: 'static' }
  | { path: '/tl/types/bots'; render: 'static' }
  | { path: '/tl/types/channels'; render: 'static' }
  | { path: '/tl/types/chatlists'; render: 'static' }
  | { path: '/tl/types/contacts'; render: 'static' }
  | { path: '/tl/types/fragment'; render: 'static' }
  | { path: '/tl/types/help'; render: 'static' }
  | { path: '/tl/types/messages'; render: 'static' }
  | { path: '/tl/types/mtproto'; render: 'static' }
  | { path: '/tl/types/payments'; render: 'static' }
  | { path: '/tl/types/phone'; render: 'static' }
  | { path: '/tl/types/photos'; render: 'static' }
  | { path: '/tl/types/premium'; render: 'static' }
  | { path: '/tl/types/smsjobs'; render: 'static' }
  | { path: '/tl/types/stats'; render: 'static' }
  | { path: '/tl/types/stickers'; render: 'static' }
  | { path: '/tl/types/storage'; render: 'static' }
  | { path: '/tl/types/stories'; render: 'static' }
  | { path: '/tl/types/updates'; render: 'static' }
  | { path: '/tl/types/upload'; render: 'static' }
  | { path: '/tl/types/users'; render: 'static' }

// prettier-ignore
declare module 'waku/router' {
  interface RouteConfig {
    paths: PathsForPages<Page>
  }
  interface CreatePagesConfig {
    pages: Page
  }
}
